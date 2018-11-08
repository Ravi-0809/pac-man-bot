# pac-man-bot
Pac man playing bot. Artificial Intelligence course project, BITS Pilani-Hyderabad Campus.  
**Note:** This project is setup and run on Ubuntu 16.04

## Basic Setup:

### 1. Installing pyenv
Used to control the python version being used. Follow the following steps:  

```
 $ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
 $ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
 $ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
 $ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
```  
**Note:** Zsh note: Modify your ~/.zshenv file instead of ~/.bash_profile. Ubuntu and Fedora note: Modify your ~/.bashrc file instead of ~/.bash_profile.  

Restart Shell for changes to take effect:
```
$ exec "$SHELL"
```

GitHub link to pyenv : https://github.com/pyenv/pyenv

### 2. Installing Python3 and setting up Virtualenv
* Installing Python3:
```
pyenv install 3.6.4
```

* Setting up virtualenv:
```
pyenv virtualenv 3.6.4 (name_of_env)
```

* Create directory and move into it  

* Assign the virtualenv to the directory
```
pyenv local (name_of_env)
```
**Note:** This will create a .python-version file that will automatically set the active VirtualEnv upon entering the directory

### 3. Installing Serpent.AI

* Go back into the folder created earlier, you should automatically enter the created VirtualEnv.
* Run `pip install SerpentAI`
* Then run 'serpent setup' to install the remaining dependencies automatically.
* GitHub link to Serpent.AI : https://github.com/SerpentAI/SerpentAI

### 4. Installing pacman
* Installing :
```
sudo apt-get update
sudo apt-get install njam
```
**Note:** We are using njam and not the normal pacman for ubuntu because of some issues with setting up in windowed mode with serpent.ai(Mentioned in the follwing sections)

* Setting up :
Run `serpent generate game`
For the name of the game prompt enter - *Njam*  
For the next prompt enter - *executable*
<!-- Window name = 'Pacman v.1.0(1995.07.18)©1995 by Roar Thronæs'  
Pacmanv.1.0(1995.07.18)©1995byRoarThronæs -->

Next, Open *plugins/SerpentNjamGamePlugin/files/serpent_Njam_game.py* and change the following:
```
kwargs["window_name"] = "Njam     http://njam.sourceforge.net"
kwargs["executable_path"] = "/usr/games/njam -w"
```

as Njam is by default in fullsceen mode, alias it to 'njam -w' in ~/.bashrc  
Enter this in ~/.bashrc : `alias njam='njam -w`  

* Run the game : `serpent launch Njam`

### 5. Installing and setting up redis  
Redis is essentially a db used to store image cache  
* redis Installation :   
```
sudo apt-get update
sudo apt-get install build-essential tcl   

cd /tmp

curl -O http://download.redis.io/redis-stable.tar.gz
tar xzvf redis-stable.tar.gz

cd redis-stable

make
make test
sudo make install
```
* Configuring redis:
```
sudo mkdir /etc/redis
sudo cp /tmp/redis-stable/redis.conf /etc/redis

sudo nano /etc/redis/redis.conf
```  
In the file, find the **supervised directive**. Currently, this is set to no. Since we are running an operating system that uses the systemd init system, we can change this to `systemd`   
Next, find the **dir** directory. Change the value to `/var/lib/redis`

* Create a redis systemd unit file:

`sudo nano /etc/systemd/system/redis.service`    
Paste the following code into it:
```
[Unit]
Description=Redis In-Memory Data Store
After=network.target

[Service]
User=redis
Group=redis
ExecStart=/usr/local/bin/redis-server /etc/redis/redis.conf
ExecStop=/usr/local/bin/redis-cli shutdown
Restart=always

[Install]
WantedBy=multi-user.target
```
* Create the redis user, group and directories:
```
sudo adduser --system --group --no-create-home redis

sudo mkdir /var/lib/redis
sudo chown redis:redis /var/lib/redis
sudo chmod 770 /var/lib/redis
```

* Start and test Redis:
```
sudo systemctl start redis

redis-cli
```
* Enable redis to start at boot:  
`sudo systemctl enable redis`

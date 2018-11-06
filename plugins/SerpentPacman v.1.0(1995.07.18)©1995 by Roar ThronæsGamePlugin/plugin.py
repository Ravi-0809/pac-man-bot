import offshoot


class SerpentPacman v.1.0(1995.07.18)©1995 by Roar ThronæsGamePlugin(offshoot.Plugin):
    name = "SerpentPacman v.1.0(1995.07.18)©1995 by Roar ThronæsGamePlugin"
    version = "0.1.0"

    libraries = []

    files = [
        {"path": "serpent_Pacman v.1.0(1995.07.18)©1995 by Roar Thronæs_game.py", "pluggable": "Game"}
    ]

    config = {
        "fps": 2
    }

    @classmethod
    def on_install(cls):
        print("\n\n%s was installed successfully!" % cls.__name__)

    @classmethod
    def on_uninstall(cls):
        print("\n\n%s was uninstalled successfully!" % cls.__name__)


if __name__ == "__main__":
    offshoot.executable_hook(SerpentPacman v.1.0(1995.07.18)©1995 by Roar ThronæsGamePlugin)

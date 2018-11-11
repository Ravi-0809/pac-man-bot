from serpent.game_agent import GameAgent
from serpent.input_controller import KeyboardKey
import numpy as np
import skimage.io
from serpent.sprite import Sprite
from serpent.sprite_locator import SpriteLocator
from serpent.sprite_identifier import SpriteIdentifier
import serpent.cv
import os
from pyautogui import press
from random import randint
import time
import pickle

class SerpentNjamGameAgent(GameAgent):

    def write_path(self):
        with open('path.pkl', 'wb') as f:
            pickle.dump(self.path_list, f)

    def read_path(self):
        with open('path.pkl', 'rb') as f:
            self.path_list = pickle.load(f)
            return self.path_list

    def identify_death(self,game_frame):
        output = self.identify_sprite(self.sprite_death, game_frame)
        return output['location']

    def traverse_path(self, random_flag):
        # Takes a random path if random_flag = 1
        if(random_flag == 1):
            directions = ['left', 'right', 'up', 'down']
            random_number = randint(0,3)
            self.path_list = self.path_list.append(directions[random_number])
            return press(directions[random_number])
        else:
            directions = self.path_list
            for d in directions:
                press(d)
                self.path_list = self.path_list.append(d)

    def sprites_init(self):
        try:
            sprites_loc = '/home/ravi/workspace/AI/pac-man-bot/plugins/SerpentNjamGamePlugin/files/data/sprites/'
        except:
            try:
                sprites_loc = '/home/ashwin/workspace/pac-man-bot/plugins/SerpentNjamGamePlugin/files/data/sprites/'
            except:
                # Achanta put your addr here.
                pass

        image_file = sprites_loc + 'sprite_pacman_left_1.png'
        image_data = skimage.io.imread(image_file)[...,np.newaxis]
        self.sprite_pacman = Sprite("Pacman", image_data=image_data)

        icon_address = ['left_2','left_3','left_4', 'right_1', 'right_2' ,'right_3' ,'right_4', 'up_1','up_2', 'up_3', 'up_4', 'down_1', 'down_2', 'down_3', 'down_4']

        for data in icon_address:
            image_file = sprites_loc + 'sprite_pacman_' + data + '.png'
            image_data = skimage.io.imread(image_file)[...,np.newaxis]
            self.sprite_pacman.append_image_data(image_data)

        image_file = sprites_loc + 'sprite_blue_0.png'
        image_data = skimage.io.imread(image_file)[..., np.newaxis]
        self.sprite_blue1 = Sprite("Blue1", image_data=image_data)

        image_file = sprites_loc + 'sprite_red_0.png'
        image_data = skimage.io.imread(image_file)[..., np.newaxis]
        self.sprite_red1 = Sprite("Red1", image_data=image_data)

        image_file = sprites_loc + 'sprite_orange_0.png'
        image_data = skimage.io.imread(image_file)[..., np.newaxis]
        self.sprite_orange1 = Sprite("Orange1", image_data=image_data)

        image_file = sprites_loc + 'sprite_death_0.png'
        image_data = skimage.io.imread(image_file)[..., np.newaxis]
        self.sprite_death = Sprite("Death", image_data=image_data)

    def identify_sprite(self, sprite, game_frame):

        sprite_identify = self.sprite_identifier.identify(sprite = sprite, mode="SIGNATURE_COLORS")
        sprite_locator = SpriteLocator()
        location = sprite_locator.locate(sprite=sprite, game_frame=game_frame)
        output = {'sprite_name' : sprite_identify, 'location':location}
        return output

    def enter_game(self):
        print('inside enter block')
        self.input_controller.tap_key(KeyboardKey.KEY_RETURN)
        self.input_controller.tap_key(KeyboardKey.KEY_RETURN)
        self.input_controller.tap_key(KeyboardKey.KEY_RETURN)
        self.c = 0

    def __init__(self, **kwargs):
        self.c = 1
        print("Inside init")
        super().__init__(**kwargs)

        self.frame_handlers["PLAY"] = self.handle_play
        self.frame_handler_setups["PLAY"] = self.setup_play

        # Initializing Sprites :
        self.sprites_init()
        self.enter_game()
        self.path_list = []

    def setup_play(self):
        pass

    def handle_play(self, game_frame):
        print("GameAgent running")

        # Dynamically setting refresh rate:
        for i, game_frame in enumerate(self.game_frame_buffer.frames):
            self.visual_debugger.store_image_data(
                game_frame.frame,
                game_frame.frame.shape,
                str(i)
            )

        l = self.read_path()
        if(len(l) == 0):
            self.traverse_path(random_flag = 1)
        else:
            self.traverse_path(random_flag = 0)

        if(self.identify_death(game_frame) != None):
            print('Game Over')
            time.sleep(3)
            self.write_path()
            print('Exiting Game')
            press('esc')
            press('esc')
            press('esc')

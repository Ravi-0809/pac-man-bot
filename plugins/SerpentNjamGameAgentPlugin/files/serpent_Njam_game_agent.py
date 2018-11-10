from serpent.game_agent import GameAgent
from serpent.input_controller import KeyboardKey
import numpy as np
import skimage.io
from serpent.sprite import Sprite
from serpent.sprite_locator import SpriteLocator

class SerpentNjamGameAgent(GameAgent):

    def sprites_init(self):
        image_file = 'datasets/collect_frames/sprite_pacman.png'
        image_data = skimage.io.imread(image_file)[..., np.newaxis]
        self.sprite_pacman = Sprite("Pacman", image_data=image_data)

        image_file = 'datasets/collect_frames/sprite_blue1.png'
        image_data = skimage.io.imread(image_file)[..., np.newaxis]
        self.sprite_blue1 = Sprite("Blue1", image_data=image_data)

        image_file = 'datasets/collect_frames/sprite_blue2.png'
        image_data = skimage.io.imread(image_file)[..., np.newaxis]
        self.sprite_blue2 = Sprite("Blue2", image_data=image_data)

        image_file = 'datasets/collect_frames/sprite_red1.png'
        image_data = skimage.io.imread(image_file)[..., np.newaxis]
        self.sprite_red1 = Sprite("Red1", image_data=image_data)

        image_file = 'datasets/collect_frames/sprite_red2.png'
        image_data = skimage.io.imread(image_file)[..., np.newaxis]
        self.sprite_red2 = Sprite("Red2", image_data=image_data)

        image_file = 'datasets/collect_frames/sprite_orange1.png'
        image_data = skimage.io.imread(image_file)[..., np.newaxis]
        self.sprite_orange1 = Sprite("Orange1", image_data=image_data)

        image_file = 'datasets/collect_frames/sprite_orange2.png'
        image_data = skimage.io.imread(image_file)[..., np.newaxis]
        self.sprite_orange2 = Sprite("Orange2", image_data=image_data)

    def __init__(self, **kwargs):
        self.c = 1
        print("Inside init")
        super().__init__(**kwargs)

        self.frame_handlers["PLAY"] = self.handle_play

        self.frame_handler_setups["PLAY"] = self.setup_play

        # Initializing Sprites :
        self.sprites_init()

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
        if self.c == 1: # Used to run only once, beginning of game. To enter the game mode.
            print('inside enter block')
            self.input_controller.tap_key(KeyboardKey.KEY_RETURN)
            self.input_controller.tap_key(KeyboardKey.KEY_RETURN)
            self.input_controller.tap_key(KeyboardKey.KEY_RETURN)
            c = 0

        # print('pacman image data = ', self.sprite_pacman.image_data)
        print('pacman image shape = ', self.sprite_pacman.image_shape)
        print('pacman sog colors = ', self.sprite_pacman.signature_colors)

        sprite_identify = self.sprite_identifier.identify(self.sprite_pacman, mode="SIGNATURE_COLORS")
        print('sprite_name = ', sprite_identify)

        sprite_locator = SpriteLocator()
        location = sprite_locator.locate(sprite=self.sprite_pacman, game_frame=game_frame)
        print('location = ', location)

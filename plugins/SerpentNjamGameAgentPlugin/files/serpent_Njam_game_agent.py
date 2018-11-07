from serpent.game_agent import GameAgent


class SerpentNjamGameAgent(GameAgent):

    def __init__(self, **kwargs):
        print("Inside init")
        super().__init__(**kwargs)

        self.frame_handlers["PLAY"] = self.handle_play

        self.frame_handler_setups["PLAY"] = self.setup_play

    def setup_play(self):
        pass

    def handle_play(self, game_frame):
        print("Testing play")

        self.input_controller.tap_key(KeyboardKey.KEY_DOWN)

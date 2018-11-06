from serpent.game import Game

from .api.api import Pacman v.1.0(1995.07.18)©1995 by Roar ThronæsAPI

from serpent.utilities import Singleton




class SerpentPacman v.1.0(1995.07.18)©1995 by Roar ThronæsGame(Game, metaclass=Singleton):

    def __init__(self, **kwargs):
        kwargs["platform"] = "executable"

        kwargs["window_name"] = "Pacmanv.1.0(1995.07.18)©1995byRoarThronæs"



        kwargs["executable_path"] = "/usr/games/pacman"



        super().__init__(**kwargs)

        self.api_class = Pacman v.1.0(1995.07.18)©1995 by Roar ThronæsAPI
        self.api_instance = None

    @property
    def screen_regions(self):
        regions = {
            "SAMPLE_REGION": (0, 0, 0, 0)
        }

        return regions

    @property
    def ocr_presets(self):
        presets = {
            "SAMPLE_PRESET": {
                "extract": {
                    "gradient_size": 1,
                    "closing_size": 1
                },
                "perform": {
                    "scale": 10,
                    "order": 1,
                    "horizontal_closing": 1,
                    "vertical_closing": 1
                }
            }
        }

        return presets

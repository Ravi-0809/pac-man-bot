from serpent.game import Game

from .api.api import NjamAPI

from serpent.utilities import Singleton
from subprocess import call




class SerpentNjamGame(Game, metaclass=Singleton):

    def __init__(self, **kwargs):
        kwargs["platform"] = "executable"
        # old_name = "Njam     http://njam.sourceforge.net"
        # new_name = "Njam"
        # call(["xdotool search --name "+old_name+" set_window --name "+new_name])
        kwargs["window_name"] = "Njam     http://njam.sourceforge.net"
        # kwargs["window_name"] = "Njam"



        kwargs["executable_path"] = "/usr/games/njam -w"



        super().__init__(**kwargs)

        self.api_class = NjamAPI
        self.api_instance = None

    @property
    def screen_regions(self):
        regions = {
            "SAMPLE_REGION": (0, 0, 0, 0),
            # "REGION": (552, 276, 573, 298)
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

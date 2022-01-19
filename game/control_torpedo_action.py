import arcade
from game import constants
from game.action import Action
from game.torpedo import Torpedo
from random import randint


class Torpedo_Action(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller
    """

    def execute(self, cast, args, director):
        spot = randint(0,1000)

        # if spot > 800:
        #     cast["torpedo"].append(Torpedo())

        # if args["key"] == arcade.key.K:
        #     cast["torpedo"].append(Torpedo())

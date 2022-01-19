import arcade
from game import constants
from game.action import Action
from game.coin import Coin
from game.coin import Coin_2
from random import randint


class Coin_action(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller
    """

    def execute(self, cast, args, director):
        spot = randint(0,1000)

        amount = 1

        if (len(cast["coins"]) <= amount):
            cast["coins"].append(Coin())

        if (len(cast["coins_2"]) <= amount):
            cast["coins_2"].append(Coin_2())



        # if spot > 800:
        #     cast["sharks"].append(Shark())
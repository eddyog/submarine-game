from game.action import Action
from game import constants

import arcade

class DrawActorsAction(Action):
    """A code template for drawing actors.
    
    Stereotype:
        Controller
    """

    def execute(self, cast, args, director):
        for submarine in cast["submarine"]:
            submarine.draw()

        for submarine in cast["submarine_2"]:
            submarine.draw()

        for coin in cast["coins"]:
            coin.draw()

        for coin_2 in cast["coins_2"]:
            coin_2.draw()

        for shark in cast["sharks"]:
            shark.draw()

        for torpedo in cast["torpedo"]:
            torpedo.draw()

        for torpedo_2 in cast["torpedo_2"]:
            torpedo_2.draw()

        for octopus in cast["octopi"]:
            octopus.draw()

        cast["score_1"][0].draw()

        cast["score_2"][0].draw()
            
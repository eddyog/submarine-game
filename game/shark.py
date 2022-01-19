import arcade
from random import randint
from game import constants


class Shark(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.SHARK_IMAGE)


        # self.center_x = 600
        # self.center_y = 500#constants.BALL_Y




        self.center_x = randint(5, constants.MAX_X - 5)
        self.center_y = 600#constants.BALL_Y
        self.change_x = 0
        self.change_y = -3




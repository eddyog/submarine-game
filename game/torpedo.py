import arcade
from game import constants


class Torpedo(arcade.Sprite):

    def __init__(self):
        super().__init__(constants.TORPEDO_IMAGE)
        self.center_x = 600
        self.center_y = 30#constants.BALL_Y
        self.change_x = 0
        self.change_y = +3

    def get_x(self,x):

        self.center_x = x

    def get_y(self,y):

        self.center_y = y





class Torpedo_2(arcade.Sprite):

    def __init__(self):
        super().__init__(constants.TORPEDO_IMAGE)
        self.center_x = 200
        self.center_y = 300#constants.BALL_Y
        self.change_x = 0
        self.change_y = +3

    def get_x(self,x):

        self.center_x = x

    def get_y(self,y):

        self.center_y = y



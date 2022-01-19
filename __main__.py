import arcade


from game import constants
from game.control_actors_action import ControlActorsAction
from game.control_shark_action import Shark_action
from game.control_coin_action import Coin_action
from game.control_torpedo_action import Torpedo_Action
from game.control_octopus_action import Octopus_action
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.play_music_action import PlayMusicAction


from game.coin import Coin
from game.coin import Coin_2
from game.shark import Shark
from game.torpedo import Torpedo
from game.torpedo import Torpedo_2 
from game.director import Director
from game.submarine import Submarine
from game.score import Score
from game.score import Score_2



def main():

    arcade.play_sound(arcade.load_sound(":resources:music/1918.mp3"))
    
    # create the cast {key: tag, value: list}
    cast = {}

    cast["submarine"] = []
    cast["submarine"].append(Submarine())

    cast["submarine_2"] = []
    cast["submarine_2"].append(Submarine())

    cast["sharks"] = []
    for i in range(constants.NUM_SHARKS):
        cast["sharks"].append(Shark())

    cast["torpedo"] = []
    cast["torpedo"].append(Torpedo())

    cast["torpedo_2"] = []
    cast["torpedo_2"].append(Torpedo_2())
    cast["octopi"] = []

    for i in range(constants.NUM_OCTOPI):
        cast["octopi"].append(Shark())

    cast["coins"] = []
    cast["coins"].append(Coin())

    cast["coins_2"] = []
    cast["coins_2"].append(Coin_2())

    cast["score_1"] = []
    cast["score_1"].append(Score())

    cast["score_2"] = []
    cast["score_2"].append(Score_2())

#    cast["sounds"] = []
#    cast["sounds"].append(arcade.Sound(':resources:music/1918.mp3'))


    
    # create the script {key: tag, value: list}
    script = {}

    control_actors_action = ControlActorsAction()
    control_shark_action = Shark_action()
    control_torpedo_action = Torpedo_Action()
    control_coin_action = Coin_action()
    control_octopus_action = Octopus_action()
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction()
    
    script[Director.ON_KEY_PRESS] = [control_actors_action, control_torpedo_action]
    script[Director.ON_UPDATE] = [control_torpedo_action, control_shark_action,control_octopus_action, control_coin_action ,move_actors_action, handle_collisions_action]
    script[Director.ON_DRAW] = [draw_actors_action]



    # start the game
    director = Director(constants.MAX_X, constants.MAX_Y)
    director.direct_scene(cast, script)
    arcade.run()


if __name__ == "__main__":
    main()





    #how to display the score. It will update it in the handle collition2
    #it will have two scores
    #Sharks will not be divide it by the screen it will be created randomly in the whole screen
    #Sharks how to delete it and add a new one so it does not create a huge list just keep 10 in the screen
    #Coins how to delete and create a new one when if have collitino or touch the button of the screeen 
    #how to create a torped and give the location of the submarine 
    #how to add a background image 
    #how to handle more than one key can be press at the time 


#self.sound = arcade.Sound(sound_file)

#self.sound.play(pan=self.pan, volume=self.volume)









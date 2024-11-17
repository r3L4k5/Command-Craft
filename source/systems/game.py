
from characters.player import Player
from systems.worldobject import WorldObject
from time import sleep

from utility import clear
from enviorment.fill_world import fill_world

class Game():

    def __init__(game) -> None:

        game.world: list[list] = [[],[],[],[],[],[],[],[],[],[],
                    [],[],[],[],[],[],[],[],[],[]]
        
        fill_world(game.world)
        
        global player
        player = Player(game.world)
              

    def update_world(game):
        
        for row in game.world:
            for tile in row:

                tile: WorldObject
                tile.update(game.world)

        for row in game.world:
            print()
            
            for tile in row:
                print(tile, end="")
        
        print(end="\n\n")
    

    def update_game(game):

        clear()

        player.display_hud()
        player.update(game.world)

        game.update_world()
        
        sleep(0.015)

        player.input_handler(game.world)

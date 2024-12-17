
from characters.player import Player
from systems.worldobject import WorldObject
from enviorment.fill_world import fill_world, spawn_player
from time import sleep
from utility import clear


class Game():

    def __init__(game) -> None:

        game.world: list[list] = [[],[],[],[],[],[],[],[],[],[],
                    [],[],[],[],[],[],[],[],[],[]]
        
        fill_world(game.world)

        game.player: Player = spawn_player(game.world)
        
        
    def update_world(game):

        for row in game.world:
            for tile in row:

                tile: WorldObject
                tile.update(game.world)

    
    def display_world(game):

        for row in game.world:
            print()
            
            for tile in row:
                print(tile, end="")
        
        print(end="\n\n")

        
    def update_game(game):

        clear()

        game.player.display_hud()

        game.update_world()
        game.display_world()
        
        sleep(0.05)

        game.player.input_handler(game.world)

        clear()

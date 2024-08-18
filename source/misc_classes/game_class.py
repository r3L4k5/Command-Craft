

from characters.player_class import Player
from enviorment.create_enviorment import fill_world
from time import sleep

class Game():

    def __init__(game) -> None:

        game.world = [[],[],[],[],[],[],[],[],[],[],
                    [],[],[],[],[],[],[],[],[],[]]
        
        game.outside = []
        
        fill_world(game.world)
        
        global player
        player = Player(game.world)
              

    def display_world(game):
        
        for row in game.world:
            print()
            
            for tile in row:
                print(tile.sprite, end="")
        
        print("\n")
    
    
    def update_game(game):
        
        player.display_hud()

        game.display_world()

        sleep(0.07)
        
        player.input_handler(game.world)


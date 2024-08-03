
import enviorment as env
import utility as uti
from player import Player


class Game():

    def __init__(game) -> None:

        game.hud = []
        
        game.world = [[],[],[],[],[],[],[],[],[],[],
                    [],[],[],[],[],[],[],[],[],[]]
        
        game.outside = []
        
        env.fill_world(game.world)
        
        game.player = Player(game.world)
              

    def display_world(game):
        
        for row in game.world:
            print()
            
            for tile in row:
                print(tile.sprite, end="")
    

    def update_game(game):
        
        game.player.display_hud()

        game.display_world()
       
        game.player.input_handler(game.world)







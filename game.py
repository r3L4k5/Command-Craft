
import enviorment as env
import utility as uti
from player import Player


class Game():

    def __init__(game) -> None:
        
        game.hud = ["100"]
        
        game.world = [[],[],[],[],[],[],[],[],[],[],
                    [],[],[],[],[],[],[],[],[],[]]
        
        env.fill_world(game.world)
        
        game.player = Player(game.world)
              
        
    def display_hud(game):
        
        print(f"{game.hud[0]:>40}")

    
    def display_world(game):
        
        for row in game.world:
            print()
            
            for tile in row:
                print(str(tile), end="")
    

    def update_game(game):
        uti.cls()
        
        game.display_hud()

        game.display_world()
       
        game.player.input_handler(game.world)




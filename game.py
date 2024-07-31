
import enviorment as env
import utility as uti
from player import Player

player = Player()


class Game():

    game_map = [[],[],[],[],[],[],[],[],[],[],
                [],[],[],[],[],[],[],[],[],[]]
    
    game_hud = ["100"]

    env.fill_map(game_map)

    player.spawn([0,5], game_map)
    
    def __init__(self_game) -> None:
        
        self_game.hud = ["100"]
        
        self_game.map = 
              
        
        
        
        

    def display_hud(self_game):
        print(f"\n{self_game.hud[0]:>40}")

    
    def display_map(self_game):
        
        for row in self_game.map:
            print()
            
            for tile in row:
                print(str(tile), end="")
    

    def update_game(self_game):
        uti.cls()
        
        self_game.display_hud()

        self_game.display_map()
       
        player.input_handler(self_game.map)





import enviorment as env
import utility as uti
from player import Player

player = Player()


class Game():
    
    def __init__(game) -> None:
        
        game.hud = ["100"]
        
        game.map = [[],[],[],[],[],[],[],[],[],[],
                    [],[],[],[],[],[],[],[],[],[]]
              
        env.fill_map(game.map)
        
        player.position = [0,10]
        game.map[0][10] = player


    def display_hud(game):
        print(f"\n{game.hud[0]:>40}")

    
    def display_map(game):
        
        for row in game.map:
            print()
            
            for tile in row:
                print(str(tile), end="")
    

    def update_game(game):
        uti.cls()
        
        game.display_hud()

        game.display_map()
       
        inp = input()

        if inp == "s":
            player.movement("down", game.map)




import enviorment as env
from os import system
from player import Player

player = Player()


class Game():
    
    def __init__(self) -> None:
        self.hud = ["100"]
        
        self.map = [[],[],[],[],[],[],[],[],[],[],
                    [],[],[],[],[],[],[],[],[],[]]
        
        env.fill_map(self.map)

    def display_hud(self):
        print(f"\n{self.hud[0]:>40}")

    
    def display_map(self):
        
        for row in self.map:
            print()
            
            for tile in row:
                print(str(tile), end="")
    

    def update_game(self):
        system("cls")
        
        player.movement(self.map)
        
        self.display_hud()

        self.display_map()
       
        input()



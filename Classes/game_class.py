

from Classes.player_class import Player
from time import sleep

class Game():

    def __init__(game) -> None:

        game.hud = []
        
        game.world = [[],[],[],[],[],[],[],[],[],[],
                    [],[],[],[],[],[],[],[],[],[]]
        
        game.outside = []
        
        import enviorment as env
        env.fill_world(game.world)
        
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

        sleep(0.05)
        
        player.input_handler(game.world)


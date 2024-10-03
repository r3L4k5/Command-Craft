

from characters.player_class import Player
from characters.npc.npc_class import NPC
from enviorment.create_enviorment import fill_world
from time import sleep
from utility import clear
from characters.npc.dog import Dog



class Game():

    def __init__(game) -> None:

        game.world: list = [[],[],[],[],[],[],[],[],[],[],
                    [],[],[],[],[],[],[],[],[],[]]

        game.npc: list[NPC] = []
        
        fill_world(game.world)

        dog = Dog(1,2)
        game.world[1][2] = dog
        game.npc.append(dog)
        
        global player
        player = Player(game.world)
              

    def display_world(game):
        
        for row in game.world:
            print()
            
            for tile in row:
                print(tile.sprite, end="")
        
        print("\n")
    
    def update_all_npc(game):
        
        for npc in game.npc:

            npc.update_npc(game.world)
    
    def update_game(game):

        clear()
        
        player.display_hud()

        game.display_world()
        
        game.update_all_npc()

        sleep(0.07)
        
        player.update_player(game.world)

        clear()


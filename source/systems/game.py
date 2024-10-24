

from characters.player import Player
from characters.npc import NPC
from enviorment.create_enviorment import fill_world
from time import sleep
from utility import clear
from characters.neutral.dog import Dog

class Game():

    def __init__(game) -> None:

        game.world: list = [[],[],[],[],[],[],[],[],[],[],
                    [],[],[],[],[],[],[],[],[],[]]

        game.npcs: list[NPC] = []
        
        fill_world(game.world)

        dog = Dog(1,2)
        game.world[1][2] = dog
        game.npcs.append(dog)
        
        global player
        player = Player(game.world)
              

    def display_world(game):
        
        for row in game.world:
            print()
            
            for tile in row:
                print(tile.sprite, end="")
        
        print("\n")
    

    def update_all_npc(game):
        
        for npc in game.npcs:

            npc.update_npc(game.world)
    

    def update_game(game):

        clear()
        
        game.update_all_npc()

        player.display_hud()

        game.display_world()
        
        player.update_player(game.world)

        clear()


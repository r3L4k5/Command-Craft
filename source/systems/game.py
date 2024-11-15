

from characters.player import Player
from characters.npc import NPC
from time import sleep

from utility import clear
from enviorment.fill_world import fill_world

class Game():

    def __init__(game) -> None:

        game.world: list[list] = [[],[],[],[],[],[],[],[],[],[],
                    [],[],[],[],[],[],[],[],[],[]]

        game.npcs: list[NPC] = []
        
        fill_world(game)
        
        global player
        player = Player(game.world)
              

    def display_world(game):
        
        for row in game.world:
            print()
            
            for tile in row:
                print(tile.sprite, end="")
        
        print(end="\n\n")
    

    def update_all_npc(game):
        
        for npc in game.npcs:

            if npc.alive() == False:

                game.npcs.remove(npc)
                npc.delete(game.world)

            npc.update_npc(game.world)
    

    def update_game(game):

        clear()
        
        game.update_all_npc()

        player.display_hud()
        player.update_player()

        game.display_world()
        
        sleep(0.015)

        player.input_handler(game.world)

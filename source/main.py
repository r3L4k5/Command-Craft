
from systems.game import Game

#The game, duh
main_game = Game()

#Game loop
while main_game.player.alive:

   main_game.update_game()


input("Game Over!")


import random
import utility as uti 

from colorama import Fore
from objects import GameObject, ObjectCategory

RESET = Fore.RESET 


class Grass(GameObject):
    
    def __init__(self, pos = []) -> None:
        super().__init__(Fore.GREEN + " ;" + RESET, pos, ObjectCategory.ENVIORMENT)


class Rock(GameObject):

    def __init__(self, pos = []) -> None:
        super().__init__( Fore.LIGHTBLACK_EX + uti.bold("()") + RESET, pos, ObjectCategory.ENVIORMENT, True)
    
    def __str__(self) -> str:
        return super().__str__()


def random_enviorment(y, x):
    probability = random.randint(1, 100)
    
    if probability == 1 and y != 0: 
        return Rock(pos= [y, x])
    else:
        return Grass(pos= [y, x])


def fill_map(map):
   
    for y in range(len(map)):
        
        for x in range(30):
            
            map[y].append(random_enviorment(y, x))
         
    return map



    



        


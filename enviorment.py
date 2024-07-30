
import random
from colorama import Fore
RESET = Fore.RESET 
from objects import GameObject, ObjectCategory

class Grass(GameObject):
    
    def __init__(self, position = []) -> None:
        super().__init__(Fore.GREEN + " ;" + RESET, position, ObjectCategory.ENVIORMENT)


class Rock(GameObject):

    def __init__(self, position = []) -> None:
        super().__init__( Fore.LIGHTBLACK_EX + "()" + RESET, position, ObjectCategory.ENVIORMENT, True)
    
    def __str__(self) -> str:
        return super().__str__()


def random_enviorment(y, x):
    probability = random.randint(1, 100)
    
    if probability == 1 and y != 0: 
        return Rock(position= [y, x])
    else:
        return Grass(position= [y, x])


def fill_map(map):
   
    for y in range(len(map)):
        for x in range(30):
            
            map[y].append(random_enviorment(y, x))
         
    return map



    



        



import random

from termcolor import colored
from objects import GameObject, ObjectCategory




class Grass(GameObject):
    
    def __init__(self, y: int = 0, x: int = 0) -> None:
        super().__init__(colored(" ;", "light_green"), y, x, ObjectCategory.ENVIORMENT)


class Rock(GameObject):

    def __init__(self, y: int = 0, x: int = 0) -> None:
        
        super().__init__(colored("()", "dark_grey", attrs=["bold"]), y, x, ObjectCategory.ENVIORMENT, True)
    

class Tree(GameObject):
    
    def __init__(self, y: int = 0, x: int = 0) -> None:
            
        super().__init__(colored("||", "red", attrs=["bold", "dark"]), y, x, ObjectCategory.ENVIORMENT, True)

        
class Leaves(GameObject):
    
    def __init__(self, y: int, x: int, world) -> None:
        
        super().__init__(colored("  ", on_color= "on_green", attrs=["bold"]), y, x, ObjectCategory.ENVIORMENT)

        world[self.y][self.x] = self


def random_enviorment(y, x, world):
    probability = random.randint(1, 100)
    
    if probability == 1 : 
        return Rock(y, x)
    
    elif 2 <= probability <= 6 and y != 0:
        Leaves(y - 1, x, world)
        return Tree(y, x)
    
    else:
        return Grass(y, x)


def fill_world(world):
   
    for y in range(len(world)):
        
        for x in range(30):
            
            world[y].append(random_enviorment(y, x, world))
         
    return world



    



        


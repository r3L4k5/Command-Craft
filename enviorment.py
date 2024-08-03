
import random

from termcolor import colored
from object_class import GameObject, ObjectCategory
import resource_class as res


class Grass(GameObject):
    
    def __init__(self, y: int = 0, x: int = 0) -> None:
        super().__init__(colored(" ;", "light_green"), y, x, ObjectCategory.ENVIORMENT)


class Rock(GameObject, res.Harvestable):

    def __init__(self, y: int = 0, x: int = 0) -> None:
        
        super().__init__(colored("()", "dark_grey", attrs=["bold"]), y, x, ObjectCategory.ENVIORMENT, True)
        res.Harvestable.__init__(self, res.Stone(), Grass())
    

class Tree(GameObject, res.Harvestable):
    
    def __init__(self, world, y: int = 0, x: int = 0) -> None:
            
        super().__init__(colored("||", "red", attrs=["bold", "dark"]), y, x, ObjectCategory.ENVIORMENT, True)
        res.Harvestable.__init__(self, res.Wood(), Grass())

        self.leaves = world[self.y - 1][self.x]
    
    """def __del__(self, world) -> None:
        
        if isinstance(self.leaves, Leaves):
            self.leaves.__del__(self, world)
        
        return super().__del__(self, world)"""


class Leaves(GameObject):
    
    def __init__(self, y: int, x: int, world) -> None:
        
        super().__init__(colored("  ", on_color= "on_green", attrs=["bold"]), y, x, ObjectCategory.ENVIORMENT)

        world[self.y][self.x] = self


def random_enviorment(y, x, world):
    probability = random.randint(1, 100)
    
    if probability == 1 : 
        return Rock(y, x)
    
    elif probability in range(1,6) and y != 0:
        
        Leaves(y - 1, x, world)
        
        return Tree(world, y, x)
    
    else:
        return Grass(y, x)


def fill_world(world):
   
    for y in range(len(world)):
        
        for x in range(30):
            
            world[y].append(random_enviorment(y, x, world))
         
    return world




    



        


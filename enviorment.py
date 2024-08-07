
import random
import Classes.resource_class as res

from termcolor import colored
from Classes.object_class import GameObject

class Grass():
    
    def __init__(self) -> None:

        self.sprite = colored(" ;", "light_green")
        self.collision = False
        
    
class Rock(GameObject, res.Harvestable):

    def __init__(self, y: int = 0, x: int = 0) -> None:
        
        super().__init__(colored("()", "dark_grey", attrs=["bold"]), y, x)
        
        res.Harvestable.__init__(self, res.Stone(), 7)
    

class Tree(GameObject, res.Harvestable):
    
    def __init__(self, y: int = 0, x: int = 0,) -> None:
            
        super().__init__(colored("||", "red", attrs=["bold", "dark"]), y, x)
        
        res.Harvestable.__init__(self, res.Wood(), 3)

    
    def delete(self, world):
        
        super().delete(world)
        
        if isinstance(world[self.y - 1][self.x], Leaves):
            
            world[self.y - 1][self.x].delete(world)


class Leaves(GameObject):
    
    def __init__(self, y: int, x: int, world = None) -> None:
        
        super().__init__(colored("  ", on_color= "on_green", attrs=["bold"]), y, x, False)

        world[self.y][self.x] = self


def random_enviorment(y, x, world):
    
    probability = random.randint(1, 100)
    
    if probability == 1 : 
        return Rock(y, x)
    
    elif probability in range(1,6) and y != 0:
        
        Leaves(y - 1, x, world)
        
        return Tree(y, x)
    
    return Grass()


def fill_world(world):
   
    for y in range(len(world)):
        
        for x in range(30):
            
            world[y].append(random_enviorment(y, x, world))
         





    



        


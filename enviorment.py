
import random
import Classes.resource_class as res
import Classes.harvestable_class as har

from termcolor import colored
from Classes.object_class import GameObject

class Grass():
    
    def __init__(self) -> None:

        self.sprite = colored(" ;", "light_green")
        self.collision = False
        
    
def random_enviorment(y, x, world):
    
    probability = random.randint(1, 100)
    
    if probability == 1 : 
        return har.Rock(y, x)
    
    elif probability in range(1,6) and y != 0:
        
        har.Leaves(y - 1, x, world)
        
        return har.Tree(y, x)
    
    return Grass()

def fill_world(world):
   
    for y in range(len(world)):
        
        for x in range(30):
            
            world[y].append(random_enviorment(y, x, world))
         





    



        


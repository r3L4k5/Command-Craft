
import  enviorment.harvestable_class as har
import enviorment.ground as env

from random import randint


def random_enviorment(y, x, world):
    
    probability = randint(1, 100)
    
    if probability == 1: 
        
        return har.Rock(y, x)
    
    elif probability in range(1,6) and y != 0:
        
        har.Leaves(y - 1, x, world)
        
        return har.Tree(y, x, world)
    
    return env.Grass()


def fill_world(world: list[list]):
   
    for y in range(len(world)):
        
        for x in range(30):
            
            world[y].append(random_enviorment(y, x, world))
    
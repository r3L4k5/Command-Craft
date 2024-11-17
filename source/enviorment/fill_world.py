
import enviorment.harvestable as har
import enviorment.ground as env

from characters.neutral.dog import Dog
from characters.npc import NPC
from systems.worldobject import WorldObject

from random import randint


def random_enviorment(y: int, x: int, world: list[list]):
    
    probability: int = randint(1, 1000)
    
    if probability in range(1, 3):

        return har.CoalOre(y, x)
    
    elif probability in range(1, 20): 
        
        return har.Rock(y, x)
    
    elif probability in range(1, 100) and y > 0:
        
        world[y - 1][x] = har.Leaves(y - 1, x)
        
        return har.Tree(y, x, world)
    
    return env.Grass(y, x)


def spawn_npc(y: int, x: int , world: list[list]):

    probability: int = randint(1, 500)

    if isinstance(world[y][x], WorldObject):
        return world[y][x]
    
    elif probability == 1:
        return Dog(y, x)
    
    return world[y][x]
    

def fill_world(world: list[list]):
   
    for y in range(len(world)):
        
        for x in range(40):
            
            world[y].append(random_enviorment(y, x, world))
    
    for y in range(len(world)):

        for x in range(len(world[y])):

            world[y][x] = spawn_npc(y, x, world)



    

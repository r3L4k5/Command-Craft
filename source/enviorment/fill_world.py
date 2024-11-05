
import enviorment.harvestable as har
import enviorment.ground as env

from characters.neutral.dog import Dog

from random import randint


def random_enviorment(y: int, x: int, world: list[list]):
    
    probability: int = randint(1, 100)
    
    if probability == 1: 
        
        return har.Rock(y, x)
    
    elif probability in range(1,6) and y != 0:
        
        har.Leaves(y - 1, x, world)
        
        return har.Tree(y, x, world)
    
    return env.Grass(y, x)


def spawn_npc(y: int, x: int , world: list[list]):

    probability = randint(1, 300)

    if probability == 1:
       
       return Dog(y, x)
    
    return world[y][x]


def fill_world(world: list[list]):
   
    for y in range(len(world)):
        
        for x in range(40):
            
            world[y].append(random_enviorment(y, x, world))
    
    for y in range(len(world)):

        for x in range(len(world[y])):

            world[y][x] = spawn_npc(y, x, world)
    

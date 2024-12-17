
import enviorment.harvestable as har
import enviorment.ground as env

from systems.worldobject import WorldObject
from characters.neutral.dog import Dog
from characters.player import Player
from characters.npc import NPC

from random import randint


def random_enviorment(y: int, x: int, world: list[list]) -> WorldObject:
    
    probability: int = randint(1, 1000)
    
    if probability in range(1, 5):

        return har.CoalOre(y, x)
    
    elif probability in range(1, 20): 
        
        return har.Rock(y, x)
    
    elif probability in range(1, 100) and y > 0:
        
        return har.Tree(y, x, world)
    
    return env.Grass(y, x)


def spawn_npc(y: int, x: int , world: list[list]) -> NPC:

    probability: int = randint(1, 500)

    if probability == 5:
        return Dog(y, x)
    
    return world[y][x]


def fill_world(world: list[list]):
   
    for y in range(len(world)):
        
        for x in range(40):

            new_enviorment: WorldObject = random_enviorment(y, x, world)
            new_enviorment.ground = env.Grass(y, x)

            #Appending instead of assigning, due to list position not existing yet
            world[y].append(new_enviorment)
    
    for y in range(len(world)):

        for x in range(len(world[y])):

            if world[y][x].collision == True:
                continue
            
            new_NPC: NPC | WorldObject = spawn_npc(y, x, world)
            new_NPC.ground = env.Grass(y, x)

            world[y][x] = new_NPC


def spawn_player(world: list[list]):

    while True:

        y = randint(0, len(world) - 1)
        x = randint(0, len(world[y]) - 1)

        if world[y][x].collision == True:
            continue
    
        break

    player: Player = Player(y, x)

    player.ground = world[y][x]
    world[y][x] = player

    return player




    

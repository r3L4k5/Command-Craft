
import enviorment.harvestable as har
import enviorment.ground as env

from systems.worldobject import WorldObject
from characters.neutral.dog import Dog
from characters.player import Player
from characters.npc import NPC
from enviorment.elements import Water

from random import randint


def create_world(size_y: int, size_x: int) -> list[list]: 

    new_world: list = []
    
    for y in range(size_y):

        row: list = []

        for x in range(size_x):

            row.append(env.Grass(y, x))
    
        new_world.append(row)
    
    filled_world = fill_world(new_world)

    return filled_world
    

def random_enviorment(y: int, x: int, world: list[list]) -> WorldObject:
    
    probability: int = randint(1, 1000)
    
    if probability in range(1, 7):

        return Water(y, x, world)
    
    elif probability in range(1, 10):

        return har.CoalOre(y, x)
    
    elif probability in range(1, 20): 
        
        return har.Rock(y, x)

    elif probability in range(1, 100) and y > 0:
        
        return har.Tree(y, x, world)
    

def spawn_npc(y: int, x: int , world: list[list]) -> NPC:

    probability: int = randint(1, 500)

    if probability == 5:
        return Dog(y, x)


def fill_world(world: list[list]):
   
    for y in range(len(world)):
        
        for x in range(len(world[y])):

            new_enviorment: WorldObject = random_enviorment(y, x, world)

            if new_enviorment is None:
                continue

            new_enviorment.behind = world[y][x]

            world[y][x] = new_enviorment
    
    for y in range(len(world)):

        for x in range(len(world[y])):

            if world[y][x].collision == True:
                continue
            
            new_NPC: NPC | WorldObject = spawn_npc(y, x, world)

            if new_NPC is None:
                continue
            
            new_NPC.behind = world[y][x]

            world[y][x] = new_NPC
    
    return world


def spawn_player(world: list[list]):

    while True:

        y = randint(0, len(world) - 1)
        x = randint(0, len(world[y]) - 1)

        if world[y][x].collision == True:
            continue
    
        break

    player: Player = Player(y, x)

    player.behind = world[y][x]
    world[y][x] = player

    return player




    

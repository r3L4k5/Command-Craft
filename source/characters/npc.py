
from characters.character import Character
from systems.worldobject import Category, WorldObject
from utility import clamp
from termcolor import colored

class NPC(WorldObject, Character):

    def __init__(self, name: str, sprite: str, y: int, x: int, health: int, strength: int, speed: int, vision: int) -> None:

        super().__init__(name, sprite, y, x, Category.NPC)
        Character.__init__(self, health, strength, speed)

        self.vision = vision


    def interact(self, object: WorldObject):
        pass

    def vision_calc(self, world):

        north_vision: int = clamp(self.y - self.vision, len(world), 0)
        south_vision: int = clamp(self.y + self.vision, len(world), 0)

        west_vision: int = clamp(self.x - self.vision, len(world[self.y]), 0)
        east_vision: int = clamp(self.x + self.vision, len(world[self.y]), 0)

        #Add 1 to south and east because when used in ex.'range(north_vision, south_vision)' in for loop, 
        #the highest number isn't included as the last number. 
        vision_field =  {"north": north_vision, "south": south_vision + 1, "west": west_vision, "east": east_vision + 1}

        return vision_field
    

    def move_toward(self, target: WorldObject, world: list):
        
        distance: list = [0,0]
        direction: str = ''

        distance[0] = target.y - self.y
        distance[1] = target.x - self.x

        if distance[0] > 1:
            direction = 'east'

        elif distance[0] < -1:
            direction = 'west'
        
        elif distance[1] > 1:
            direction = 'south'
        
        elif distance[1] < - 1:
            direction = "north"
        
        else:
            return
    
        self.movement(direction, world)
    
    def update_npc(self, world):
        pass
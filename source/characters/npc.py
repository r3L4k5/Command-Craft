
from characters.character import Character
from systems.worldobject import ObjectCategory, WorldObject
from utility import clamp


class NPC(WorldObject, Character):

    def __init__(self, name: str, sprite: str, y: int, x: int, health: int, strength: int, speed: int, vision: int) -> None:

        super().__init__(name, sprite, y, x, ObjectCategory.NPC)
        Character.__init__(self, health, strength, speed)

        self.vision = vision


    def interact(self, object: WorldObject):
        pass


    def vision_calc(self, world):

        north_vision: int = clamp(self.y - self.vision, len(world) - 1, 0)
        south_vision: int = clamp(self.y + self.vision, len(world) - 1, 0)

        west_vision: int = clamp(self.x - self.vision, len(world[self.y]) - 1, 0)
        east_vision: int = clamp(self.x + self.vision, len(world[self.y]) - 1, 0)

        #Add 1 to south and east because when used in ex.'range(north_vision, south_vision)' in for loop, 
        #the highest number isn't included as the last number. 
        vision_field =  {"north": north_vision, "south": south_vision + 1, "west": west_vision, "east": east_vision + 1}

        return vision_field
    

    def move_toward(self, target: WorldObject, world: list):
        
        if target.name == "player":

            distance: list = {"y-axis": 0, "x-axis": 0}
            direction: str = ''

            distance["y-axis"] = target.y - self.y
            distance["x-axis"] = target.x - self.x

            if distance["y-axis"] > 1:
                direction = 'south'

            elif distance["y-axis"] < -1:
                direction = 'north'
            
            elif distance["x-axis"] > 1:
                direction = 'east'
            
            elif distance["x-axis"] < - 1:
                direction = "west"
            
            else:
                return

            self.movement(direction, world)
                
                
    def update_npc(self, world):
        pass

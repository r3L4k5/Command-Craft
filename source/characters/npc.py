
from characters.character import Character
from systems.worldobject import WorldObject
from utility import clamp
from random import choice

class NPC(Character):

    def __init__(self, name: str, sprite: str, y: int, x: int, health: int, strength: int, speed: int, 
                 vision: int, loot: list | None = None) -> None:

        super().__init__(name, sprite, y, x, True, health, strength, speed)

        self.vision = vision
        self.loot = loot
    

    def vision_calc(self, world):

        north_vision: int = clamp(self.y - self.vision, len(world) - 1, 0)
        south_vision: int = clamp(self.y + self.vision, len(world) - 1, 0)

        west_vision: int = clamp(self.x - self.vision, len(world[self.y]) - 1, 0)
        east_vision: int = clamp(self.x + self.vision, len(world[self.y]) - 1, 0)

        #Add 1 to south and east because when used in ex.'range(north_vision, south_vision)' in for loop, 
        #the highest number isn't included as the last number. 
        vision_field =  {"north": north_vision, "south": south_vision + 1, "west": west_vision, "east": east_vision + 1}

        return vision_field


    def detection(self, world: list[list]):

        vision_field = self.vision_calc(world)
        targets: dict =  {}

        for y in range(vision_field["north"], vision_field["south"]):
            for x in range(vision_field["west"], vision_field["east"]):

                targets[world[y][x].name] = world[y][x]
            
        return targets
                
            
    def move_toward(self, world: list[list]):

        targets: dict = self.detection(world)

        
        if "player" in targets:

            target: Character = targets["player"]

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
        
        else: 
            random_direction = choice(["north", "south", "west", "east"])
            self.movement(random_direction, world)


    def react(self, actor: Character, world: list[list], friendly: bool):
        pass


    def update_npc(self, world: list[list]):

        self.detection(world)
        self.move_toward(world)

        return self.alive()


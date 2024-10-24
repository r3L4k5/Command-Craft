
from systems.worldobject import WorldObject, ObjectCategory
from characters.npc import NPC

class Dog(NPC):

    def __init__(self, y: int, x: int) -> None:

        super().__init__("dog", " m", y, x, 100, 10, 1, 3)


    def interact(self, object: WorldObject):
        
        if object.name == "player":
            print("Woof >:(")

    
    def detection(self, world: list):

        vision_field = super().vision_calc(world)

        for y in range(vision_field["north"], vision_field["south"]):
            for x in range(vision_field["west"], vision_field["east"]):
                
                self.move_toward(world[y][x], world)


    def update_npc(self, world):
        self.detection(world)

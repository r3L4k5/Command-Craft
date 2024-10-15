
from systems.worldobject import WorldObject, Category
from characters.npc import NPC

class Dog(NPC):

    def __init__(self, y: int, x: int) -> None:

        super().__init__("dog", " m", y, x, 100, 10, 1, 3)

    def interact(self, object: WorldObject):
        input("Woof >:(")
    
    def detection(self, world: list):

        vision_field = super().vision_calc(world)

        for y in range(vision_field["north"], vision_field["south"]):
            for x in range(vision_field["west"], vision_field["east"]):
                
                if world[y][x].name == "player":
                    self.move_toward(world[y][x])

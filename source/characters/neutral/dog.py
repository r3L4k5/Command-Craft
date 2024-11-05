
from items.item_access import get_item
from characters.npc import NPC
from characters.character import Character


class Dog(NPC):

    def __init__(self, y: int, x: int) -> None:

        super().__init__("dog", " m", y, x, 5, 1, 1, 3, [get_item("wood")])
    
    def react(self, actor: Character, world: list):
        input("Ruff!")
    
    def detection(self, world: list):

        vision_field = self.vision_calc(world)

        for y in range(vision_field["north"], vision_field["south"]):
            for x in range(vision_field["west"], vision_field["east"]):
                
                self.move_toward(world[y][x], world)


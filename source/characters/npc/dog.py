
from systems.object_class import WorldObject, Category
from characters.npc.npc_class import NPC
from termcolor import colored
from utility import clamp

class Dog(WorldObject, NPC):

    def __init__(self, y: int, x: int) -> None:

        super().__init__("dog", " m", y, x, Category.ENEMY)
        NPC.__init__(self, 100, 10, 1, 3)

    def interact(self, object: WorldObject):

        if object.category == Category.PLAYER:
            self.sprite = colored(self.sprite, "red")
            object.health = 50
    
    def detection(self, world):

        up_vision: int = clamp(self.y - self.vision, len(world), 0)
        down_vision: int = clamp(self.y + self.vision, len(world), 0)

        left_vision: int = clamp(self.x - self.vision, len(world[self.y]), 0)
        right_vision: int = clamp(self.x - self.vision, len(world[self.y]), 0)
        
        for y in range(up_vision, down_vision):
            for x in range(left_vision, right_vision):

                self.interact(world[x][y])

    def update_npc(self, world):
        self.detection(world)

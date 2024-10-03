
from systems.object_class import WorldObject, Category
from characters.npc.npc_class import NPC
from termcolor import colored
from utility import clamp

class Dog(WorldObject, NPC):

    def __init__(self, y: int, x: int) -> None:

        super().__init__("dog", " m", y, x, Category.ENEMY)
        NPC.__init__(self, 100, 10, 1, 3)


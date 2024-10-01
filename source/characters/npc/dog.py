
from systems.object_class import WorldObject, Category
from characters.npc.npc_class import NPC
from termcolor import colored

class Dog(WorldObject, NPC):

    def __init__(self, y: int, x: int) -> None:

        super().__init__("dog", " m", y, x, Category.ENEMY)

    def interact(self):
        print("nah")

if __name__ == "__main__":

    Dog(1,2).interact()
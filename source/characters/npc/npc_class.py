
from characters.character_class import Character
from systems.object_class import Category, WorldObject
from utility import clamp
from termcolor import colored

class NPC(Character):

    def __init__(self, health: int, strength: int, speed: int, vision: int) -> None:

        super().__init__(health, strength, speed)

        self.vision = vision

    def interact(self, object: WorldObject):
        
        if object.sprite == " i":
            self.sprite = colored(self.sprite, "red")
        
    def detection(self, world):

        up_vision: int = clamp(self.y - self.vision, len(world), 0)
        down_vision: int = clamp(self.y + self.vision, len(world), 0)

        left_vision: int = clamp(self.x - self.vision, len(world[self.y]), 0)
        right_vision: int = clamp(self.x + self.vision, len(world[self.y]), 0)

        #Add 1 because the stop number is not included
        #otherwise y and x will never reach max range
        for y in range(up_vision, down_vision + 1):
            for x in range(left_vision, right_vision + 1):
                 
                self.interact(world[y][x])
        
    
    def update_npc(self, world):
        self.detection(world)





                










        
        


if __name__ == "__main__":
    pass





    
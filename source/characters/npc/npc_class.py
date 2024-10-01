
from characters.character_class import Character
from utility import clamp


class NPC(Character):

    def __init__(self, world: list, health: int, strength: int, speed: int, vision: int) -> None:

        super().__init__(health, strength, speed)

        self.vision = vision

    def vision_area(self, world):

        up_vision: int = clamp(self.y - self.vision, len(world), 0)
        down_vision: int = clamp(self.y + self.vision, len(world), 0)
        left_vision: int = clamp(self.x - self.vision, len(world[self.y]), 0)
        right_vision: int = clamp(self.x - self.vision, len(world[self.y]), 0)
        
        for y in range(up_vision, down_vision):
            for x in range(left_vision, right_vision):

                self.interact(world[y][x])

    
    def interact(self, object):
        pass
    
    def update_npc(self, world):
        self.vision_area(world)





                










        
        


if __name__ == "__main__":
    pass





    
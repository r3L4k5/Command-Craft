
from enum import Enum, auto
from enviorment.ground import Grass


class ObjectCategory(Enum):
    HARVESTABLE = auto()
    PLAYER = auto()
    NPC = auto()
 

class WorldObject():
    
    def __init__(self, name: str, sprite: str, y: int, x: int, category: ObjectCategory, collision: bool = True) -> None:
        
        self.sprite = sprite
        self.collision = collision
        self.category = category
        self.name = name
        
        self.y = y
        self.x = x

        self.ground = Grass(y, x)
        

    def __str__(self) -> str:
        return f"{self.sprite}"
    
    
    def delete(self, world) -> None:
        
        world[self.y][self.x] = self.ground
        del self

    
    


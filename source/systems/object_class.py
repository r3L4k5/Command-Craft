
from enum import Enum, auto
from enviorment.ground import Grass


class Category(Enum):
    
    RESOURCES = auto()
    HARVESTABLE = auto()
    GROUND = auto()
    PLAYER = auto()
    ENEMY = auto()
    CRAFTABLE = auto()


class WorldObject():
    
    def __init__(self, name: str, sprite: str, y: int, x: int, category: Category, collision: bool = True) -> None:
        
        self.sprite = sprite
        self.collision = collision
        self.category = category
        self.name = name
        
        self.ground = Grass()
        
        self.y = y
        self.x = x

    def __str__(self) -> str:
        return f"{self.sprite}"
    
    def delete(self, world) -> None:
        
        world[self.y][self.x] = self.ground
        del self

    
    



from enum import Enum, auto

class ObjectCategory(Enum):
    ENVIORMENT = auto()
    PLAYER = auto()
    ENEMY = auto()


class GameObject():
    def __init__(self, sprite: str, y: int, x: int,  category: ObjectCategory, collision: bool = False) -> None:
        
        self.sprite = sprite
        self.category = category
        self.collision = collision
        self.y = y
        self.x = x
    
    def __str__(self) -> str:
        return self.sprite
    


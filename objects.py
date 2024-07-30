
from enum import Enum, auto

class ObjectCategory(Enum):
    ENVIORMENT = auto()
    PLAYER = auto()
    ENEMY = auto()


class GameObject():
    def __init__(self, sprite: str, position: list[int], category: ObjectCategory, collision: bool = False) -> None:
        
        self.sprite = sprite
        self.position = position
        self.category = category
        self.collision = collision
    
    def __str__(self) -> str:
        return self.sprite
    


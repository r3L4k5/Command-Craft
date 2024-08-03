
from enum import Enum, auto

def enviorment_import():
    import enviorment

    return enviorment


class ObjectCategory(Enum):
    HARVESTABLE = auto()
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
    
    
    


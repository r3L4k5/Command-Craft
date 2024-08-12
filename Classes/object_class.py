
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
    
    def __init__(self, sprite: str, y: int, x: int, collision: bool = True) -> None:
        
        self.sprite = sprite
        self.collision = collision
        
        self.ground = enviorment_import().Grass()
        
        self.y = y
        self.x = x

    def __str__(self) -> str:
        return f"{self.sprite}"
    
    def delete(self, world):
        
        world[self.y][self.x] = self.ground
        del self

    
    


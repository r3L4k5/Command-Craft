
from enum import Enum, auto

class Material(Enum):
    WOOD = auto(),
    STONE = auto(),
    NONE = auto


class Item():
    
    def __init__(self, name: str, sprite: str, material: Material = Material.NONE, amount: int = 1) -> None:
        
        self.name: str = name
        self.sprite: str = sprite
        self.amount: int = amount
        self.material: Material = material
    
    def effect():
        pass
    
    def __str__(self) -> str:
        return self.sprite
    
    def __eq__(self, value: object) -> bool:
        return type(self) == type(value)



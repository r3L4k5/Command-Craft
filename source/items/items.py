
from enum import Enum, auto

class Material(Enum):
    WOOD = auto(),
    STONE = auto(),
    NONE = auto

class ItemCategory(Enum):
    RESOURCE = auto(),
    CRAFTABLE = auto()


class Item():
    
    def __init__(self, name: str, sprite: str, category: ItemCategory, material: Material = Material.NONE, amount: int = 1) -> None:
        
        self.name: str = name
        self.sprite: str = sprite
        self.amount: int = amount
        self.category: ItemCategory = category
        self.material: Material = material
    
    def __str__(self) -> str:
        return self.sprite
    
    def __eq__(self, value: object) -> bool:
        return type(self) == type(value)



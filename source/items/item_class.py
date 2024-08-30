
from misc_classes.object_class import Category

class Item():
    
    def __init__(self, name: str, sprite: str, category: Category, amount: int = 1, ) -> None:
        
        self.name: str = name
        self.sprite: str = sprite
        self.amount: int = amount
        self.category: Category = category

    def __str__(self) -> str:
        return self.sprite
    
    def __eq__(self, value: object) -> bool:
        return type(self) == type(value)
    

    

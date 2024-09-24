
from items.item_class import Item
from termcolor import colored
from system.object_class import Category


class Sword(Item):

    def __init__(self, material, recipe: dict, damage: int, durability: int) -> None:
        
        super().__init__("sword", colored("\\", material.color, attrs= [material.brightness, "bold"]), Category.TOOLS, 1)
        
        self.durability = durability
        self.material = material
        self.recipe: dict = recipe
        self.damage: int = damage

    def __eq__(self, value: object) -> bool:
        
        if type(self) == type(value) and self.material == value.material:
            return True

    def attack():
        pass


class Axe(Item):
    
    def __init__(self, name: str, sprite: str, category: Category, amount: int = 1) -> None:
        super().__init__(name, sprite, category, amount)

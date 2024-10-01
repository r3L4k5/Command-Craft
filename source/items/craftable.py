
from items.item_class import Item
from termcolor import colored
from systems.object_class import Category


class Sword(Item):

    def __init__(self, material, recipe: dict, damage: int, durability: int) -> None:
        
        super().__init__("sword", colored("\\", material.color, attrs= [material.brightness, "bold"]), Category.CRAFTABLE)
        
        self.material = material
        self.recipe: dict = recipe
        self.damage: int = damage
        self.durability: int = durability

    def __eq__(self, value: object) -> bool:
        
        if type(self) == type(value) and self.material == value.material:
            return True
        
    def effect():
        pass


class Axe(Item):
    
    def __init__(self, name: str, sprite: str, category: Category) -> None:
        
        super().__init__(name, sprite, category)

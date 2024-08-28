
from materials.items.item_class import Item
from termcolor import colored
from misc_classes.object_class import Category


class Sword(Item):

    def __init__(self, material, recipe: dict, damage: int, durability: int, amount: int = 1) -> None:
        
        super().__init__("Sword", colored("\\", material.color, attrs= [material.brightness, "bold"]), Category.TOOLS, amount)
        
        self.durability = durability
        self.material = material
        self.recipe: dict = recipe
        self.damage: int = damage
    
    def __eq__(self, value: object) -> bool:
        
        if type(self) == type(value) and self.material == value.material:
            return True

    def attack():
        pass


from materials.items.item_class import Item
from termcolor import colored
from misc_classes.object_class import Category


class Sword(Item):

    def __init__(self, material, amount: int = 1) -> None:
        
        super().__init__("Sword", colored("\\", material["color"], attrs= material["attrs"]), Category.TOOLS, amount)
        
        self.recipe: dict 
        self.damage: int 
    
    def attack():
        pass

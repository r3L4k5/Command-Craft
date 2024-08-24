
from materials.items.item_class import Item
from termcolor import colored

class Sword(Item):

    def __init__(self, name: str = "Sword", sprite: str = "\\", amount: int = 1) -> None:
        
        super().__init__(name, sprite, amount)
        self.sprite = colored(sprite, "grey", attrs= ["bold"])
        self.recipe = {"Wood": 3}

 
sword = Sword()    


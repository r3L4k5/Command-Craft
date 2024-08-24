
from materials.item_class import Item
from termcolor import colored

class Tool(Item):

    def __init__(self, name: str = "Sword", sprite: str = "\ ", amount: int = 1) -> None:
        
        super().__init__(name, sprite, amount)
        
        self.recipe = {"Wood": 3}

 
sword = Tool("Sword", colored("/", "grey"))    


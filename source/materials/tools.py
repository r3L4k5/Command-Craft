
from materials.item_class import Item
from materials.resources import resource_dict 

class Tool(Item):

    def __init__(self, name: str, sprite: str, amount: int) -> None:
        super().__init__(name, sprite, amount)
        
        self.recipe = {type(resource_dict["Wood"]): 3}

 
sword = Tool("Sword", "]", 3)    

print(sword.recipe)
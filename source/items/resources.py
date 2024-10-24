
from termcolor import colored
from items.items import Item, Material, ItemCategory


class Wood(Item):
    
    def __init__(self, amount: int = 1):
        
        super().__init__("wood", colored("||", "red", attrs=["bold", "dark"]), ItemCategory.RESOURCE, Material.WOOD, amount)
        

class Stone(Item):
    
    def __init__(self, amount: int = 1):
        
        super().__init__("stone", colored("()", "dark_grey", attrs=["bold"]), ItemCategory.RESOURCE, Material.STONE, amount)

        
        
            
        
        
       

    



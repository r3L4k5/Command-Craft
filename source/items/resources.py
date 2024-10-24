
from termcolor import colored
from items.items import Item, Material


class Wood(Item):
    
    def __init__(self, amount: int = 1):
        
        super().__init__("wood", colored("||", "red", attrs=["bold", "dark"]), Material.WOOD, amount)
        

class Stone(Item):
    
    def __init__(self, amount: int = 1):
        
        super().__init__("stone", colored("()", "dark_grey", attrs=["bold"]), Material.STONE, amount)

        
        
            
        
        
       

    



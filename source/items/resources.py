
from termcolor import colored
from items.items import Item, Material


class Wood(Item):
    
    def __init__(self, amount: int = 1):
        
        super().__init__("wood", colored("||", "red", attrs=["bold", "dark"]), Material.WOOD, amount)
        

class Stone(Item):
    
    def __init__(self, amount: int = 1):
        
        super().__init__("stone", colored("()", "grey", attrs=["bold"]), Material.MINERAL, amount)


class Coal(Item):

    def __init__(self, amount: int = 1):

        super().__init__("coal", colored(" C", color="dark_grey", attrs=["bold", "dark"]), Material.MINERAL, amount)

        
        
            
        
        
       

    



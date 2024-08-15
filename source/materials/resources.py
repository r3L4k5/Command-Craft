
from termcolor import colored

from materials.item_class import Item

class Wood(Item):
    
    def __init__(self, amount: int = 1):
        super().__init__("Wood", colored("||", "red", attrs=["bold", "dark"]), amount)

class Stone(Item):
    
    def __init__(self, amount: int = 1):
        super().__init__("Stone", colored("()", "dark_grey", attrs=["bold"]), amount)


resource_dict = {
    
    "Wood": Wood(),
    "Stone": Stone(),
}

            
        
            
        
        
       

    



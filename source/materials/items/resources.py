
from termcolor import colored

from misc_classes.object_class import Category
from materials.items.item_class import Item


class Wood(Item):
    
    def __init__(self, amount: int = 1):
        
        super().__init__("Wood", colored("||", "red", attrs=["bold", "dark"]), Category.RESOURCES, amount)
        


class Stone(Item):
    
    def __init__(self, amount: int = 1):
        
        super().__init__("Stone", colored("()", "dark_grey", attrs=["bold"]), Category.RESOURCES, amount)

        
        
            
        
        
       

    



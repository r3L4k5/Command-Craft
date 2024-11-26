
from termcolor import colored
from items.items import Item


class Wood(Item):
    
    def __init__(self, amount: int = 1):
        
        super().__init__("wood", colored("||", "red", attrs=["bold", "dark"]), False, amount)
        

class Stone(Item):
    
    def __init__(self, amount: int = 1):
        
        super().__init__("stone", colored("()", "grey", attrs=["bold"]), False,  amount)


class Coal(Item):

    def __init__(self, amount: int = 1):

        super().__init__("coal", colored(" C", color="dark_grey", attrs=["bold", "dark"]), False, amount)

        
        
            
        
        
       

    



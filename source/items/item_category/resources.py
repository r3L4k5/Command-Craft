
import termcolor as ter
from items.items import Item


class Wood(Item):
    
    def __init__(self, amount: int = 1):
        
        super().__init__("wood", ter.colored("||", "red", attrs=["bold", "dark"]), amount)
        

class Stone(Item):
    
    def __init__(self, amount: int = 1):
        
        super().__init__("stone", ter.colored("()", "grey", attrs=["bold"]), amount)


class Coal(Item):

    def __init__(self, amount: int = 1):

        super().__init__("coal", ter.colored(" C", color="dark_grey", attrs=["bold", "dark"]), amount)


class Leather(Item):

    def __init__(self, amount = 1):

        super().__init__("leather", ter.colored("[]", color="red", attrs=["dark", "bold"]), amount)

        
        
            
        
        
       

    



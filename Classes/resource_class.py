
from termcolor import colored

class Resource():
    
    def __init__(self, name: str, sprite:  str, amount: int = 1):
        
        self.name: str = name
        self.sprite: str = sprite
        self.amount: int = amount
    
    def __str__(self) -> str:
        return self.sprite

class Wood(Resource):
    
    def __init__(self, amount: int = 1):
        super().__init__("Wood", colored("||", "red", attrs=["bold", "dark"]), amount)

class Stone(Resource):
    
    def __init__(self, amount: int = 1):
        super().__init__("Stone", colored("()", "dark_grey", attrs=["bold"]), amount)


resource_dict = {
    
    "Wood": Wood(),
    "Stone": Stone(),
}

            
        
            
        
        
       

    



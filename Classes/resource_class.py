
from termcolor import colored


class Resource():
    
    def __init__(self, name: str, sprite:  str):
        
        self.name: str = name
        self.sprite: str = sprite
        self.amount: int = 1
    
    def __str__(self) -> str:
        return self.sprite

class Wood(Resource):
    
    def __init__(self):
        super().__init__("Wood", colored("||", "red", attrs=["bold", "dark"]))

class Stone(Resource):
    
    def __init__(self):
        super().__init__("Stone", colored("()", "dark_grey", attrs=["bold"]))


resource_dict = {
    
    "Wood": Wood(),
    "Stone": Stone(),
}

            
class Harvestable():
    
    def __init__(self, resource: object, hitpoints: int ):
        
        self.hitpoints = hitpoints
        self.resource = resource

    def harvest(self, player, world):
        
        if self.hitpoints > 1:
            
            self.hitpoints -= player.strength
            print(self.hitpoints)
            
            return

        for item in player.inventory:
            
            if self.resource.name == item.name and item.amount < 2:
                
                item.amount += 1
                self.delete(world)
                
                return

        player.inventory.append(self.resource)
        self.delete(world)

        
            
        
        
       

    



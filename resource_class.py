
from termcolor import colored


class Wood():
    
    def __init__(self):
        self.sprite = colored("||", "red", attrs=["bold", "dark"])
        self.name = "Wood"
    
    def __str__(self) -> str:
        return self.name

class Stone():
    
    def __init__(self):
        self.sprite = colored("()", "dark_grey", attrs=["bold"])
        self.name = "Stone"
        
    
    def __str__(self) -> str:
        return self.name
    

class Harvestable():
    
    def __init__(self, resource: object, ground, hitpoints: int ):
        
        self.hitpoints = hitpoints
        self.resource = resource
        self.ground = ground
    

    def harvest(self, player, world):
        
        if self.hitpoints > 1:
            
            self.hitpoints -= player.stats.strength
            print(self.hitpoints)
            
            return

        duplicates = [slot for slot in player.inventory if str(slot["item"]) == self.resource.name ]

        if len(duplicates) == 0:
            
            inventory_slot = {"item": self.resource, "amount": 1}
            player.inventory.append(inventory_slot)
        
        else:
            duplicates[0]["amount"] += 1
        
        
        world[self.y][self.x] = self.ground
        
        del self

    



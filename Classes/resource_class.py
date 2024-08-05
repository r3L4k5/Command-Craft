
from termcolor import colored


class Wood():
    
    def __init__(self):
        
        self.sprite = colored("||", "red", attrs=["bold", "dark"])
        self.name = "Wood"
    

class Stone():
    
    def __init__(self):
        
        self.sprite = colored("()", "dark_grey", attrs=["bold"])
        self.name = "Stone"
        
    
class Harvestable():
    
    def __init__(self, resource: object, hitpoints: int ):
        
        self.hitpoints = hitpoints
        self.resource = resource

    def harvest(self, player, world):
        
        if self.hitpoints > 1:
            
            self.hitpoints -= player.stats.strength
            print(self.hitpoints)
            
            return

        for slot in player.inventory:
            
            if self.resource.name == slot["item"].name and slot["amount"] < 20:
                
                slot["amount"] += 1
                self.delete(world)
                
                return

        new_inventory_slot = {"item": self.resource, "amount": 1}
        player.inventory.append(new_inventory_slot)

        self.delete(world)
            
        
        
       

    




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
    
    def __init__(self, resource: object, ground):
        
        self.resource = resource
        self.ground = ground
    

    def __del__(self, world) -> None:
    
        world[self.y][self.x] = self.ground
        
        del self
    
    
    def harvest(self, inventory, world):

        duplicates = [slot for slot in inventory if str(slot["item"]) == self.resource.name ]

        if len(duplicates) == 0:
            
            inventory_slot = {"sprite": self.resource.sprite, "item": self.resource, "amount": 1}
            
            inventory.append(inventory_slot)
        
        else:
            duplicates[0]["amount"] += 1
        

        self.__del__(world)

    



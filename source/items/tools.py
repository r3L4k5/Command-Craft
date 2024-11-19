
from items.items import Item
from systems.worldobject import WorldObject, Material
from termcolor import colored
from enum import Enum, auto

class Resource(Enum):
    WOOD = auto(),
    STONE = auto(),

def resource_color(sprite: str, resource: str) -> str:

    match resource:

        case Resource.WOOD:
            return colored(sprite, "red", attrs=["bold", "dark"])
        
        case Resource.STONE:
            return colored(sprite, "dark_grey", attrs=["bold", "dark"])
        
        case _:
            raise "Resource not found"


class Tool(Item):
    
    def __init__(self, name: str, sprite: str, resource: Resource, recipe: dict, durability: int, power: int) -> None:
        
        super().__init__(name, resource_color(sprite, resource))

        self.recipe = recipe
        self.durability = durability
        self.resource = resource
        self.power = power

    #Temporary solution:
    #Predefined target parameter because it is not needed and to avoid error when 
    #calling the shared effect() while harvesting. Otherwise target argument 
    #would be given without corresponding parameter in certain cases 
    def effect(self, player: WorldObject, target: Item | WorldObject = None):
        
        power: int = self.power

        if self.durability == 1:
            player.equipped = None
            del self
        
        self.durability -= 1
        return power


    def __eq__(self, value: object) -> bool:
        
        if type(self) == type(value) and self.resource == value.resource:
            return True
        
    
class Sword(Tool):

    def __init__(self, resource: Resource, recipe: dict, durability: int, power: int) -> None:
        
        super().__init__("sword", "/", resource, recipe, durability, power)

    #Same as base class regarding target = None 
    def effect(self, player: WorldObject, target = None):

        if target is None:
            return super().effect(player)
        
        #Default is None and cannot be multiplied with players strength;
        #rather 1 to not effect strength whilst not causing errors
        return 1
    

class Axe(Tool):
    
    def __init__(self, resource: Resource, recipe: dict, durability: int, power: int) -> None:
        
        super().__init__("axe", "P", resource, recipe, durability, power)
    
    def effect(self, player: WorldObject, target: WorldObject):
        
        if target.material == Resource.WOOD:
            
            return super().effect(player)
        
        return 1
        

class Pickaxe(Tool):

    def __init__(self, resource: Resource, recipe: dict, durability: int, power: int) -> None:
        
        super().__init__("pickaxe", "T", resource, recipe, durability, power)
    
    def effect(self, player: WorldObject, target: WorldObject):

        if target.material == Material.MINERAL:

            return super().effect(player)
        
        return 1
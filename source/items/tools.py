
from items.items import Item, Material
from systems.worldobject import WorldObject
from termcolor import colored


def material_color(sprite: str, material: str) -> str:

    match material:

        case Material.WOOD:
            return colored(sprite, "red", attrs=["bold", "dark"])
        
        case Material.STONE:
            return colored(sprite, "dark_grey", attrs=["bold"])
        
        case _:
            raise "Material not found"


class Tool(Item):
    
    def __init__(self, name: str, sprite: str, material: Material, recipe: dict, durability: int, power: int) -> None:
        
        super().__init__(name, material_color(sprite, material), material)

        self.recipe = recipe
        self.durability = durability
        self.material = material
        self.power = power

    #Temporary solution:
    #Predefined target parameter because it is not needed and to avoid error when 
    #calling the shared effect() while harvesting. Otherwise target argument 
    #would be given without corresponding parameter in certain cases 
    def effect(self, player: WorldObject, target: Item | WorldObject = None):
        
        if self.durability == 1:

            #Tools power stored in variable, due to not beeing
            #accesible after deletion of item
            power: int = self.power 

            player.equipped = None
            del self    

            return power
        
        self.durability -= 1
        return self.power


    def __eq__(self, value: object) -> bool:
        
        if type(self) == type(value) and self.material == value.material:
            return True
        
    
class Sword(Tool):

    def __init__(self, material: Material, recipe: dict, durability: int, power: int) -> None:
        
        super().__init__("sword", "/", material, recipe, durability, power)

    #Same as base class regarding target = None 
    def effect(self, player: WorldObject, target = None):

        if target is None:
            return super().effect(player)
        
        #Default is None and cannot be multiplied with players strength;
        #rather 1 to not effect strength whilst not causing errors
        return 1
    

class Axe(Tool):
    
    def __init__(self, material: Material, recipe: dict, durability: int, power: int) -> None:
        
        super().__init__("axe", "P", material, recipe, durability, power)
    
    def effect(self, player, target):
        
        if target.material == Material.WOOD:
            
            return super().effect(player)
        
        return 1
        

class Pickaxe(Tool):

    def __init__(self, material: Material, recipe: dict, durability: int, power: int) -> None:
        
        super().__init__("pickaxe", "T", material, recipe, durability, power)
    
    def effect(self, player, target):

        if target.material == Material.STONE:

            return super().effect(player)
        
        return 1
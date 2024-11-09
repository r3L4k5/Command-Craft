
from unicodedata import category
from items.items import Item, Material
from systems.worldobject import ObjectCategory
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

    #Returns 1 instead of default due to strength attribute of player being multiplied 
    #by the return value of the function. Default Nonetype return leads to error, 
    #so 1 is returned instead.
    def effect(self, target):
        return 1 


    def __eq__(self, value: object) -> bool:
        
        if type(self) == type(value) and self.material == value.material:
            return True
        
    
class Sword(Tool):

    def __init__(self, material: str, recipe: dict, durability: int, power: int) -> None:
        
        super().__init__("sword", "/", material, recipe, durability, power)

    #Temporary solution:
    #Predefined target parameter to avoid error when calling the shared effect()
    #while harvesting. Otherwise target argument would be given without corresponding
    #parameter. 
    def effect(self, target = None):

        if target is None:

            self.durability -= 1
            return self.power
        
        super().effect(target)
        
    
class Axe(Tool):
    
    def __init__(self, material: str, recipe: dict, durability: int, power: int) -> None:
        
        super().__init__("axe", "P", material, recipe, durability, power)
    
    def effect(self, target):
        
        if target.material == Material.WOOD:
            
            self.durability -= 1
            return self.power
        
        super().effect(target)
        

class Pickaxe(Tool):

    def __init__(self, material: str, recipe: dict, durability: int, power: int) -> None:
        
        super().__init__("pickaxe", "T", material, recipe, durability, power)
    
    def effect(self, target):

        if target.material == Material.STONE:

            self.durability -= 1
            return self.power
        
        super().effect(target)
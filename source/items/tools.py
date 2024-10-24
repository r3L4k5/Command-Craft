
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


    def effect(self, target):
        pass


    def __eq__(self, value: object) -> bool:
        
        if type(self) == type(value) and self.material == value.material:
            return True
        
    
class Sword(Tool):

    def __init__(self, material: str, recipe: dict, durability: int, power: int) -> None:
        
        super().__init__("sword", "/", material, recipe, durability, power)
    
    def effect(self, target):
        
        if target.category == ObjectCategory.NPC:
            return self.power
        
    
class Axe(Tool):
    
    def __init__(self, material: str, recipe: dict, durability: int, power: int) -> None:
        
        super().__init__("axe", "P", material, recipe, durability, power)
    
    def effect(self, target):
        
        if target.material == Material.WOOD:
            return self.power
        

class Pickaxe(Tool):

    def __init__(self, material: str, recipe: dict, durability: int, power: int) -> None:
        
        super().__init__("pickaxe", "T", material, recipe, durability, power)
    
    def effect(self, target):

        if target.material == Material.STONE:
            return self.power
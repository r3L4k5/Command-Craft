
from items.items import Item
from termcolor import colored
from systems.worldobject import Category


def material_color(sprite: str, material: str) -> str:

    match material:

        case "wood":
            return colored(sprite, "red", attrs=["bold", "dark"])
        
        case "stone":
            return colored(sprite, "dark_grey", attrs=["bold", "dark"])
        
        case _:
            raise "Material not found"


class Tool(Item):
    
    def __init__(self, name: str, sprite: str, material: str, recipe: dict, durability: int, damage: int) -> None:
        
        super().__init__(name, material_color(sprite, material), Category.CRAFTABLE)

        self.recipe = recipe
        self.durability = durability
        self.material = material
        self.damage = damage
    

    def __eq__(self, value: object) -> bool:
        
        if type(self) == type(value) and self.material == value.material:
            return True
    

    def effect():
        pass
        
    
class Sword(Tool):

    def __init__(self, material: str, recipe: dict, durability: int, damage: int) -> None:
        
        super().__init__("sword", "/", material, recipe, durability, damage)
        
    
class Axe(Tool):
    
    def __init__(self, material: str, recipe: dict, durability: int, damage: int) -> None:
        
        super().__init__("axe", "P", material, recipe, durability, damage)
    

class Pickaxe(Tool):

    def __init__(self, material: str, recipe: dict, durability: int, damage: int) -> None:
        super().__init__("pickaxe", "T", material, recipe, durability, damage)
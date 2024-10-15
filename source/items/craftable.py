
from items.items import Item
from termcolor import colored
from systems.worldobject import Category


def color_to_material(sprite, material) -> str:

    match material:

        case "wood":
            return colored(sprite, "red", attrs=["bold", "dark"])
        
        case "stone":
            return colored(sprite, "dark_grey", attrs=["bold", "dark"])
        
        case _:
            raise "Materialnot found"


class Sword(Item):

    def __init__(self, material: str, recipe: dict, damage: int, durability: int) -> None:
        
        super().__init__("sword", color_to_material("\\", material), Category.CRAFTABLE)
        
        self.material = material
        self.recipe: dict = recipe
        self.damage: int = damage
        self.durability: int = durability

    def __eq__(self, value: object) -> bool:
        
        if type(self) == type(value) and self.material == value.material:
            return True
        
    def effect():
        pass


class Axe(Item):
    
    def __init__(self, name: str, sprite: str, category: Category) -> None:
        
        super().__init__(name, sprite, category)

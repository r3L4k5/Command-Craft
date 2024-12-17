
from items.items import Item
from items.craftable import Craftable
from systems.worldobject import WorldObject, Material
from characters.character import Character
from characters.npc import NPC

from termcolor import colored
from enum import Enum, auto


class Resource(Enum):
    WOOD = auto(),
    STONE = auto()


def resource_color(sprite: str, resource: str) -> str:

    match resource:

        case Resource.WOOD:
            return colored(sprite, "red", attrs=["bold", "dark"])
        
        case Resource.STONE:
            return colored(sprite, "dark_grey", attrs=["bold", "dark"])
        
        case _:
            raise "Resource not found"


class Tool(Item, Craftable):
    
    def __init__(self, name: str, sprite: str, resource: Resource, recipe: dict, durability: int, power: int) -> None:
        
        super().__init__(name, resource_color(sprite, resource), False, False)

        Craftable.__init__(self, recipe)

        self.durability = durability
        self.resource = resource
        self.power = power

    def effect(self, world: list[list], actor: Character, target: WorldObject): 

        actor.strength *= self.power

        target.interacted(actor, world)

        actor.strength /= self.power
        
        self.durability -= 1
        
        if self.durability == 0:
            del self
            
            
    def __eq__(self, value: object) -> bool:
        
        if type(self) == type(value) and self.resource == value.resource:
            return True
        
    
class Sword(Tool):

    def __init__(self, resource: Resource, recipe: dict, durability: int, power: int) -> None:
        
        super().__init__("sword", "/", resource, recipe, durability, power)


    def effect(self, world: list[list], actor: Character, target: NPC):

        if target.material == Material.FLESH:

            actor.strength *= self.power

            target.interacted(actor, world, False)

            actor.strength /= self.power

            if target.health == 0:

                target.drop_loot(actor)


class Axe(Tool):
    
    def __init__(self, resource: Resource, recipe: dict, durability: int, power: int) -> None:
        
        super().__init__("axe", "P", resource, recipe, durability, power)
    
    def effect(self, world: list[list], actor: WorldObject, target: WorldObject):
        
        if target.material == Material.PLANT:

            super().effect(world, actor, target)
        

class Pickaxe(Tool):

    def __init__(self, resource: Resource, recipe: dict, durability: int, power: int) -> None:
        
        super().__init__("pickaxe", "T", resource, recipe, durability, power)
    
    def effect(self, world: list[list], actor: WorldObject, target: WorldObject):

        if target.material == Material.MINERAL:

            super().effect(world, actor, target)

            

        
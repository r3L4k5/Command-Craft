
from items.items import Item
from items.craftable import Craftable
from systems.worldobject import WorldObject, Material
from characters.character import Character
from characters.npc import NPC

import termcolor as ter
from enum import Enum, auto


class Resource(Enum):
    WOOD = auto(),
    STONE = auto()


def resource_color(sprite: str, resource: str) -> str:

    match resource:

        case Resource.WOOD:
            return ter.colored(sprite, "red", attrs=["bold", "dark"])
        
        case Resource.STONE:
            return ter.colored(sprite, "dark_grey", attrs=["bold", "dark"])
        
        case _:
            raise "Resource not found"


class Tool(Item, Craftable):
    
    def __init__(self, name: str, sprite: str, resource: Resource, recipe: dict, durability: int, power: int) -> None:
        
        super().__init__(name, resource_color(sprite, resource))

        Craftable.__init__(self, recipe)

        self.durability = durability
        self.resource = resource
        self.power = power

    def equipped_effect(self, world: list[list], actor: Character, target: WorldObject): 

        actor.strength *= self.power

        if target.material == Material.FLESH:
            target.interacted(actor, world, False)

        else:
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


    def equipped_effect(self, world: list[list], actor: Character, target: NPC):

        if target.material == Material.FLESH:

            super().equipped_effect(world, actor, target)

            if target.health == 0:
                target.drop_loot(actor)


class Axe(Tool):
    
    def __init__(self, resource: Resource, recipe: dict, durability: int, power: int) -> None:
        
        super().__init__("axe", "P", resource, recipe, durability, power)
    
    def equipped_effect(self, world: list[list], actor: WorldObject, target: WorldObject):
        
        if target.material == Material.PLANT:

            super().equipped_effect(world, actor, target)
        

class Pickaxe(Tool):

    def __init__(self, resource: Resource, recipe: dict, durability: int, power: int) -> None:
        
        super().__init__("pickaxe", "T", resource, recipe, durability, power)
    
    def equipped_effect(self, world: list[list], actor: WorldObject, target: WorldObject):

        if target.material == Material.MINERAL:

            super().equipped_effect(world, actor, target)

            

        

import items.resources as res
import enviorment.ground as gro

from systems.worldobject import WorldObject
from characters.character import Character
from items.tools import Tool
from items.items import Item
from termcolor import colored


class Harvestable(WorldObject):
    
    def __init__(self, name: str, sprite: str, y: int, x: int, 
                 hitpoint: int, resource: Item) -> None:
        
        super().__init__(name, sprite, y, x)

        self.hitpoint = hitpoint
        self.resource = resource

    def harvest(self, actor: Character, world: list[list]):

        total_strength: int = actor.strength

        if isinstance(actor.equipped, Tool):

            total_strength *= actor.equipped.effect(actor, self.resource)
   
        if self.hitpoint - total_strength > 0:

            self.hitpoint -= total_strength
            return
            
        actor.inventory.add_item(self.resource)
        
        self.delete(world)
        

class Tree(Harvestable):
    
    def __init__(self, y: int, x: int, world: list[list]) -> None:
            
        super().__init__("tree", colored("||", "red", attrs=["bold", "dark"]), y, x, 7, res.Wood(3))

        for i in range(1, self.y + 1):

            if isinstance(world[self.y - i][self.x], Leaves):
                continue

            else:
                self.resource.amount = (i - 1) * 3
                break
    
    def delete(self, world) -> None:

        for i in range(1, self.y + 1):

            above: WorldObject = world[self.y - i][self.x]

            if isinstance(above, Leaves):
                above.delete(world)
            
            elif isinstance(above, Character):
                above.ground = Leaves(above.y, above.x)
            
            else:
                break
        
        super().delete(world)
            
class Leaves(WorldObject):
    
    def __init__(self, y: int, x: int) -> None:
        
        super().__init__("leaves", colored("  ", on_color= "on_green", attrs=["bold"]), y, x, False)

    def update(self, world):

        if len(world) < 20:
            return
        
        elif isinstance(world[self.y + 1][self.x], Tree):
            return
        
        elif isinstance(world[self.y + 1][self.x], Leaves):
            return
            
        self.delete(world)
    

class Rock(Harvestable):

    def __init__(self, y: int, x: int) -> None:
        
        super().__init__("rock", colored("()", "dark_grey", attrs=["bold", "dark"]), y, x, 15, res.Stone(3))


class CoalOre(Harvestable):

    def __init__(self, y: int, x: int) -> None:

        super().__init__("coal", colored(" C", "dark_grey", attrs=["bold", "dark"]), y, x, 20, res.Coal(3))


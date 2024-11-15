
import items.resources as res
import enviorment.ground as gro

from systems.worldobject import WorldObject
from characters.character import Character
from items.tools import Tool
from items.items import Item
from termcolor import colored


class Harvestable(WorldObject):
    
    def __init__(self, name: str, sprite: str, y: int, x: int, 
                 hitpoint: int, resource: Item, collision: bool = True) -> None:
        
        super().__init__(name, sprite, y, x, collision)

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
            
        super().__init__("tree", colored("||", "red", attrs=["bold", "dark"]), y, x, 3, res.Wood())

        for i in range(1, self.y):

            if isinstance(world[self.y - i][self.x], Leaves):

                self.resource.amount += 1

                
    def delete(self, world: list[list]):
        
        super().delete(world)
        
        for i in range(1, self.y):

            above: WorldObject = world[self.y - i][self.x]

            if isinstance(above, Leaves):

                above.delete(world)
            
            elif isinstance(above, Character):
        
                above.ground = gro.Grass(above.y, above.x) 

            else: 
                break
           
      
class Leaves(WorldObject):
    
    def __init__(self, y: int, x: int) -> None:
        
        super().__init__("leaves", colored("  ", on_color= "on_green", attrs=["bold"]), y, x, False)


class Rock(Harvestable):

    def __init__(self, y: int, x: int) -> None:
        
        super().__init__("rock", colored("()", "dark_grey", attrs=["bold", "dark"]), y, x, 7, res.Stone())


class CoalOre(Harvestable):

    def __init__(self, y: int, x: int) -> None:
        super().__init__("coal", colored(" C", "dark_grey", attrs=["bold", "dark"]), y, x, 9, res.Coal())


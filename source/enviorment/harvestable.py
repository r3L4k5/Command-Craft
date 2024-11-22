
import items.resources as res

from systems.worldobject import WorldObject, Material
from characters.character import Character
from items.items import Item
from termcolor import colored


class Harvestable(WorldObject):
    
    def __init__(self, name: str, sprite: str, y: int, x: int, 
                 hitpoint: int, resource: Item, material: Material) -> None:
        
        super().__init__(name, sprite, y, x, material)

        self.hitpoint = hitpoint
        self.resource = resource

    def interacted(self, actor: Character, world: list[list]):
   
        if self.hitpoint - actor.strength > 0:
            self.hitpoint -= actor.strength
            return
            
        actor.inventory.add_item(self.resource)
        
        self.delete(world)
        

class Tree(Harvestable):
    
    def __init__(self, y: int, x: int, world: list[list]) -> None:
            
        super().__init__("tree", colored("||", "red", attrs=["bold", "dark"]), y, x, 8, res.Wood(3), Material.PLANT)

        for i in range(1, self.y + 1):

            if isinstance(world[self.y - i][self.x], Leaves):
                continue

            else:
                self.resource.amount = (i - 1) * 3
                break
    
    def delete(self, world: list[list]) -> None:

        super().delete(world)

        for i in range(1, self.y + 1):

            above: WorldObject = world[self.y - i][self.x]

            if isinstance(above, Leaves):
                above.delete(world)
            
            elif isinstance(above, Character):
                above.ground = Leaves(above.y, above.x)
            
            else:
                break
        
        
class Leaves(WorldObject):
    
    def __init__(self, y: int, x: int) -> None:
        
        super().__init__("leaves", colored("  ", on_color= "on_green", attrs=["bold"]), y, x, Material.PLANT, False)
    

class Rock(Harvestable):

    def __init__(self, y: int, x: int) -> None:
        
        super().__init__("rock", colored("()", "dark_grey", attrs=["bold", "dark"]), y, x, 15, res.Stone(3), Material.MINERAL)


class CoalOre(Harvestable):

    def __init__(self, y: int, x: int) -> None:

        super().__init__("coal", colored(" C", "dark_grey", attrs=["bold", "dark"]), y, x, 20, res.Coal(3), Material.MINERAL)


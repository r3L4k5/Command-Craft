
import items.resources as res
import enviorment.ground as gro

from systems.worldobject import WorldObject, ObjectCategory
from characters.character import Character
from items.tools import Tool
from items.items import Item
from termcolor import colored


class Harvestable():
    
    def __init__(self, resource: Item, hitpoints: int ):
        
        self.hitpoints = hitpoints
        self.resource = resource


    def harvest(self, player: WorldObject | Character, world):

        total_strength: int = player.strength

        if isinstance(player.equipped, Tool):

            total_strength *= player.equipped.effect(self.resource)
        
        if self.hitpoints - total_strength > 0:

            self.hitpoints -= total_strength
            return
            
        player.inventory.add_item(self.resource)
        
        self.delete(world)


class Rock(WorldObject, Harvestable):

    def __init__(self, y: int, x: int) -> None:
        
        super().__init__("rock", colored("()", "dark_grey", attrs=["bold"]), y, x, ObjectCategory.HARVESTABLE)
        
        Harvestable.__init__(self, res.Stone(), 7)


class Tree(WorldObject, Harvestable):
    
    def __init__(self, y: int, x: int, world) -> None:
            
        super().__init__("tree", colored("||", "red", attrs=["bold", "dark"]), y, x, ObjectCategory.HARVESTABLE)
        
        Harvestable.__init__(self, res.Wood(), 3)

        for i in range(1, self.y):

            if isinstance(world[self.y - i][self.x], Leaves):
                continue
                
            else:
                self.resource.amount = i - 1
                break

                
    def delete(self, world):
        
        super().delete(world)
        
        for i in range(1, self.y):

            above: WorldObject = world[self.y - i][self.x]

            if isinstance(above, Leaves):

                above.delete(world)
            
            elif isinstance(above, cha.Character):
        
                above.ground = gro.Grass(above.y, above.x) 

            else: 
                break
           
      
class Leaves(WorldObject):
    
    def __init__(self, y: int, x: int, world = None) -> None:
        
        super().__init__("leaves", colored("  ", on_color= "on_green", attrs=["bold"]), y, x, ObjectCategory.HARVESTABLE, False)

        world[self.y][self.x] = self

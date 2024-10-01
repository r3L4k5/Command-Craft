
import items.resources as res
import characters.character_class as cha
import enviorment.ground as gro

from systems.object_class import WorldObject, Category
from termcolor import colored


class Harvestable():
    
    def __init__(self, resource: object, hitpoints: int ):
        
        self.hitpoints = hitpoints
        self.resource = resource

    def harvest(self, player: WorldObject , world):
        
        if self.hitpoints > 1:
            
            self.hitpoints -= player.strength
            return

        player.inventory.add_item(self.resource)
        
        self.delete(world)


class Rock(WorldObject, Harvestable):

    def __init__(self, y: int = 0, x: int = 0) -> None:
        
        super().__init__("rock", colored("()", "dark_grey", attrs=["bold"]), y, x, Category.HARVESTABLE )
        
        Harvestable.__init__(self, res.Stone(), 7)


class Tree(WorldObject, Harvestable):
    
    def __init__(self, y: int, x: int, world) -> None:
            
        super().__init__("tree", colored("||", "red", attrs=["bold", "dark"]), y, x, Category.HARVESTABLE)
        
        Harvestable.__init__(self, res.Wood(), 3)

        for i in range(1, self.y):

            if isinstance(world[self.y - i][self.x], Leaves):
                continue
                
            else:
                self.reamount = i - 1
                break

                
    def delete(self, world):
        
        super().delete(world)
        
        for i in range(1, self.y):

            above = world[self.y - i][self.x]
        
            if isinstance(above, Leaves):

                above.delete(world)
            
            elif isinstance(above, cha.Character):
        
                above.ground = gro.Grass() 
            
            else: 
                break
           
      
class Leaves(WorldObject):
    
    def __init__(self, y: int, x: int, world = None) -> None:
        
        super().__init__("leaves", colored("  ", on_color= "on_green", attrs=["bold"]), y, x, Category.HARVESTABLE, False)

        world[self.y][self.x] = self

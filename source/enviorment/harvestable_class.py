
import items.resources as res
import characters.character_class as cha
import enviorment.ground as gro

from misc_classes.object_class import WorldObject, Category
from termcolor import colored


class Harvestable():
    
    def __init__(self, resource: object, hitpoints: int ):
        
        self.hitpoints = hitpoints
        self.resource = resource

    def harvest(self, player: WorldObject, world):
        
        if self.hitpoints > 1:
            
            self.hitpoints -= player.strength
            return

        player.inventory.add_item(self.resource)
        
        self.delete(world)


class Rock(WorldObject, Harvestable):

    def __init__(self, y: int = 0, x: int = 0) -> None:
        
        super().__init__(colored("()", "dark_grey", attrs=["bold"]), y, x, Category.HARVESTABLE )
        
        Harvestable.__init__(self, res.Stone(), 7)


class Tree(WorldObject, Harvestable):
    
    def __init__(self, y: int, x: int, world) -> None:
            
        super().__init__(colored("||", "red", attrs=["bold", "dark"]), y, x, Category.HARVESTABLE)
        
        Harvestable.__init__(self, res.Wood(), 3)

        for i in range(1, self.y):

            if isinstance(world[self.y - i][self.x], Leaves):
                continue
                
            else:
                self.resource.amount = i - 1
                break

                
    def delete(self, world):
        
        super().delete(world)
        
        for i in range(0, self.y):

            above = world[self.y - i][self.x]
        
            if isinstance(above, Leaves):

                world[self.y - i][self.x].delete(world)
            
            elif isinstance(above, cha.Character):
        
                world[self.y - i][self.x].ground = gro.Grass() 
            
            else: 
                break
           
      
class Leaves(WorldObject):
    
    def __init__(self, y: int, x: int, world = None) -> None:
        
        super().__init__(colored("  ", on_color= "on_green", attrs=["bold"]), y, x, Category.HARVESTABLE, False)

        world[self.y][self.x] = self

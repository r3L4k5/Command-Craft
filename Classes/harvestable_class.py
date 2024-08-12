
import Classes.resource_class as res

from Classes.object_class import GameObject
from termcolor import colored



class Harvestable():
    
    def __init__(self, resource: object, hitpoints: int ):
        
        self.hitpoints = hitpoints
        self.resource = resource

    def harvest(self, player, world):
        
        if self.hitpoints > 1:
            
            self.hitpoints -= player.strength
            return

        player.inventory.add_item(self.resource)
        
        self.delete(world)


class Rock(GameObject, Harvestable):

    def __init__(self, y: int = 0, x: int = 0) -> None:
        
        super().__init__(colored("()", "dark_grey", attrs=["bold"]), y, x)
        
        Harvestable.__init__(self, res.Stone(), 7)


class Tree(GameObject, Harvestable):
    
    def __init__(self, y: int = 0, x: int = 0,) -> None:
            
        super().__init__(colored("||", "red", attrs=["bold", "dark"]), y, x)
        
        Harvestable.__init__(self, res.Wood(), 3)

    
    def delete(self, world):
        
        super().delete(world)
        
        if isinstance(world[self.y - 1][self.x], Leaves):
            
            world[self.y - 1][self.x].delete(world)


class Leaves(GameObject):
    
    def __init__(self, y: int, x: int, world = None) -> None:
        
        super().__init__(colored("  ", on_color= "on_green", attrs=["bold"]), y, x, False)

        world[self.y][self.x] = self

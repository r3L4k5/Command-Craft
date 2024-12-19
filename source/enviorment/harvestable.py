
import termcolor as ter
import random as ran

from systems.worldobject import WorldObject, Material
from characters.character import Character
from enviorment.ground import Grass
from items.items import Item
from items.item_access import get_item
from utility import clamp


class Harvestable(WorldObject):
    
    def __init__(self, name: str, sprite: str, y: int, x: int, 
                 hitpoint: int, loot: list[Item], material: Material) -> None:
        
        super().__init__(name, sprite, y, x, material)

        self.hitpoint = hitpoint
        self.loot = loot

    def interacted(self, actor: Character, world: list[list]):
   
        if self.hitpoint - actor.strength > 0:

            self.hitpoint -= actor.strength
            return
        
        for item in self.loot:
            actor.inventory.add_item(item)
        
        self.delete(world)
        

class Tree(Harvestable):
    
    def __init__(self, y: int, x: int, world: list[list]) -> None:
            
        super().__init__("tree", ter.colored("||", "red", attrs=["bold", "dark"]), y, x, 8, [get_item("wood", 3)], Material.PLANT)

        self.height = ran.randint(1, clamp(self.y, max=3))

        self.loot[0].amount *= self.height

        #Spawn leaves above tree
        for i in range(1, self.height + 1):

            if isinstance(world[self.y - i][self.x], Tree | Leaves):
                
                break

            else:
                leaves = Leaves(self.y - i, self.x)
                leaves.behind = world[self.y - i][self.x]
                
                world[self.y - i][self.x] = leaves
        
        #25% chance to drop apples after getting chopped down
        if ran.randint(1, 4) == 1:

            self.loot.append(get_item("fruit", 2 * self.height))
        

    def delete(self, world: list[list]) -> None:

        super().delete(world)

        for i in range(1, self.height + 1):

            above: WorldObject = world[self.y - i][self.x]

            if isinstance(above, Leaves):
                above.delete(world)
            
            elif isinstance(above, Character):
                above.behind = Grass(above.y, above.x)
            
            else:
                break
        

class Leaves(WorldObject):
    
    def __init__(self, y: int, x: int) -> None:
        
        super().__init__("leaves", ter.colored("||", on_color= "on_green", attrs=["bold"]), y, x, Material.PLANT, False)

        self.in_air = True
    

class Rock(Harvestable):

    def __init__(self, y: int, x: int) -> None:
        
        super().__init__("rock", ter.colored("()", "dark_grey", attrs=["bold", "dark"]), y, x, 15, [get_item("stone", 3)], Material.MINERAL)


class CoalOre(Harvestable):

    def __init__(self, y: int, x: int) -> None:

        super().__init__("coalore", ter.colored(" C", "dark_grey", attrs=["bold", "dark"]), y, x, 20, [get_item("coal", 2)], Material.MINERAL)


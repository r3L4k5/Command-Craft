
from items.items import Item
from items.craftable import Craftable
from systems.worldobject import WorldObject
from enviorment.elements import Fire
from characters.character import Character

import termcolor as ter
import copy as cop

class Torch(Item, Craftable):

    def __init__(self, amount: int = 1) -> None:

        super().__init__("torch", 
                         ter.colored("/", color="red", attrs=["bold", "dark"]) + 
                         ter.colored("*", color="yellow", attrs=["bold", "dark"]), 
                         amount)

        Craftable.__init__(self, {"wood": 1, "coal": 1})
    

    def equipped_effect(self, world: list[list], actor: Character, target: WorldObject):

        target: WorldObject = actor.get_target(world)

        Fire(target, world)
        
        self.delete(actor.inventory, actor.equipped)

    
    def inventory_effect(self, world: list[list], actor: Character, target: WorldObject):

        target: WorldObject = actor.get_target(world)

        Fire(target, world)
        
        self.delete(actor.inventory, actor.equipped)


class Shoes(Item, Craftable):

    def __init__(self, amount = 1):

        super().__init__("shoes", ter.colored("L", color="red", attrs=["dark", "bold"]), amount)  

        Craftable.__init__(self, {"leather": 2})


    def passive_effect(self, world: list[list], actor: Character, target: WorldObject | None = None):

        if actor.equipped == self and actor.speed == actor.base_speed:

            actor.speed *= 2

        else: 
            actor.speed = actor.base_speed


class Bucket(Item, Craftable):

    def __init__(self, amount = 1):

        super().__init__("bucket", ter.colored("U", color="red", attrs=["bold", "dark"]), amount)

        Craftable.__init__(self, {"wood": 6})

        self.content: WorldObject | None  = None

    def equipped_effect(self, world: list[list], actor: Character, target: WorldObject):

        if self.content is None:

            self.content = target
            world[target.y][target.x] = target.behind 

            self.name = f"bucket ({self.content.name.capitalize()})"

        else:
            self.content.y = target.y
            self.content.x = target.x

            self.content.behind = target.behind
            world[target.y][target.x] = self.content

            self.name = "bucket"
            self.content = None 

            
        




        
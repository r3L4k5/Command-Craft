
from items.items import Item
from items.craftable import Craftable
from systems.worldobject import WorldObject
from enviorment.elements import Fire
from characters.character import Character

from termcolor import colored

class Torch(Item, Craftable):

    def __init__(self, amount: int = 1) -> None:

        super().__init__("torch", 
                         colored("/", color="red", attrs=["bold", "dark"]) + 
                         colored("*", color="yellow", attrs=["bold", "dark"]), 
                         True, False, amount)

        Craftable.__init__(self, {"wood": 1, "coal": 1})
    

    def effect(self, world: list[list], actor: Character, target: WorldObject):
        
        target: WorldObject = actor.get_target(world)

        Fire(target, world)

        if self == actor.equipped:
            actor.equipped = None

        else:
            actor.inventory.remove_item(self)
        
        self.delete(actor.inventory, actor.equipped)


class Shoes(Item, Craftable):

    def __init__(self, amount = 1):

        super().__init__("shoes", colored("L", color="red", attrs=["dark", "bold"]), False, True, amount)  

        Craftable.__init__(self, {"leather": 2})


    def effect(self, world: list[list], actor: Character, target: WorldObject | None = None):

        if actor.equipped == self and actor.speed == actor.base_speed:

            actor.speed *= 2

        else: 
            actor.speed = actor.base_speed


            
        




        
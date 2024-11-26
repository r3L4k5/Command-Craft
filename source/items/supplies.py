
from items.items import Item
from systems.worldobject import WorldObject
from enviorment.fire import Fire
from characters.character import Character

from termcolor import colored


class Torch(Item):

    def __init__(self, amount: int = 1) -> None:

        super().__init__("torch", 
                         colored("/", color="red", attrs=["bold", "dark"]) + 
                         colored("*", color="yellow", attrs=["bold", "dark"]), 
                         True, amount)

        self.recipe: dict = {"wood": 1, "coal": 1}
    

    def effect(self, world: list[list], actor: Character, target: WorldObject):
        
        target: WorldObject = actor.get_target(world)

        Fire(target, world)

        if self == actor.equipped:
            actor.equipped = None
        else:
            actor.inventory.remove_item(self)

        

            
        




        
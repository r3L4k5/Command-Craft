
from items.items import Item
from characters.character import Character
from systems.worldobject import WorldObject
from enviorment.fire import Fire

from termcolor import colored


class Torch(Item):

    def __init__(self, amount: int = 1) -> None:

        super().__init__("torch", 
                         colored("/", color="red", attrs=["bold", "dark"]) + 
                         colored("*", color="yellow", attrs=["bold", "dark"]), 
                         amount)

        self.recipe: dict = {"wood": 1, "coal": 1}
    

    def effect(self, player: Character, world: list[list]):
        
        target: WorldObject | object = player.get_target(world)

        Fire(target, world)

        if player.equipped == self:
            player.equipped = None

        else:
            player.inventory.remove_item(self)

            
        




        
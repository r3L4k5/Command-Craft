
from items.items import Item, Material
from characters.character import Character
from systems.worldobject import WorldObject
from enviorment.fire import Fire

from termcolor import colored


class Torch(Item):

    def __init__(self, amount: int = 1) -> None:

        super().__init__("torch", 
                         colored("/", color="red", attrs=["bold", "dark"]) + 
                         colored("*", color="yellow", attrs=["bold", "dark"]), 
                         Material.NONE, amount)

        self.recipe: dict = {"wood": 1, "coal": 1}
    

    def effect(self, player: Character, world: list[list]):
        
        target: WorldObject | object = player.target_register(world)

        fire: WorldObject = Fire(target.y, target.x)

        if isinstance(target, WorldObject):

            fire.ground = target.ground
            target.delete(world)
        
        world[fire.y][fire.x] = fire

            
        




        
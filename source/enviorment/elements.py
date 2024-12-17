
from systems.worldobject import WorldObject, Material
from characters.character import Character

from termcolor import colored
from random import choice


class Fire(WorldObject):
    
    def __init__(self, target: WorldObject, world: list[list]) -> None:
        
        super().__init__("fire", colored("ww", color= "yellow", on_color="on_red", attrs=["bold"]), target.y, target.x, Material.MISC, False)

        self.spread_timer: int = 25
        self.ground = target.ground

        target.delete(world)
        
        world[self.y][self.x] = self


    def fires_nearby(self, world: list[list]) -> int:

        fires: int = 1

        if isinstance(self.get_target(world, "north"), Fire):
            fires += 1
        
        elif isinstance(self.get_target(world, "south"), Fire):
            fires += 1

        elif isinstance(self.get_target(world, "west"), Fire):
            fires += 1
        
        elif isinstance(self.get_target(world, "east"), Fire):
            fires += 1
        
        return fires


    def spread(self, world: list[list]):

        if self.spread_timer > 0:
            self.spread_timer -= int(5 / self.fires_nearby(world))
            return
        
        else:
            direction: str = choice(["north", "south", "west", "east"])

            target: WorldObject = self.get_target(world, direction)

            if target is not (None or isinstance(target, Fire)):

                Fire(target, world)

            self.spread_timer = 25


    def damage(self, world: list[list]):

        target: WorldObject = self.get_target(world)

        if isinstance(target, Character):
            target.health -= 2


    def update(self, world: list[list]):

        self.spread(world)
        self.damage(world)

        
        
         

        
        





        
    

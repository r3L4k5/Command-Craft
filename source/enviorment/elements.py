
import termcolor as ter
import random as ran

from systems.worldobject import WorldObject, Material
from characters.character import Character


class Fire(WorldObject):
    
    def __init__(self, target: WorldObject, world: list[list]) -> None:

        if target.material != (Material.FLESH and Material.PLANT):
            return
        
        super().__init__("fire", ter.colored("ww", color= "yellow", on_color="on_red", attrs=["bold"]), target.y, target.x, Material.MISC, False)

        self.spread_timer: int = 25
        self.behind = target.behind

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
            direction: str = ran.choice(["north", "south", "west", "east"])

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

        
class Water(WorldObject):

    def __init__(self, y: int, x: int, world: list[list], core : bool= True):

        super().__init__("water", ter.colored("~~", on_color="on_blue", attrs=["dark"]), y, x, Material.MISC, False)

        self.size: int = ran.randint(8, 15)

        if not core:
            return

        for _ in range(self.size):

            direction = ran.choice(["north", "south", "east", "west"])

            target: WorldObject = self.get_target(world, direction)

            if target is None or target.collision == True:
                continue

            elif target.in_air:
                target.behind = self

            elif isinstance(target, Water):
                continue

            else:
                new_water = Water(y, x, world, False)
                new_water.behind = target.behind

                world[target.y][target.x] = new_water

        
        
        





        
    

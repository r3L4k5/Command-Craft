
from systems.worldobject import WorldObject
from termcolor import colored
from random import choice, randint


class Fire(WorldObject):
    
    def __init__(self, target: WorldObject, world: list[list]) -> None:

        if isinstance(target, WorldObject) and target.collision == False:

            return
        
        super().__init__("fire", colored("ww", color= "yellow", on_color="on_red", attrs=["bold"]), target.y, target.x, False)

        self.spread_time: int = 25

        if isinstance(target, WorldObject):

            self.ground = target.ground
            target.delete(world)
   
        else:
            self.ground = target
        
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


    def update(self, world: list[list]):

        
        if self.spread_time > 0:

            self.spread_time -= int(5 / self.fires_nearby(world))
            return
        
        else:
            direction: str = choice(["north", "south", "west", "east"])

            target: WorldObject = self.get_target(world, direction)

            if target is not None and not isinstance(target, Fire):

                Fire(target, world)

            self.spread_time = 25

         

        
        





        
    

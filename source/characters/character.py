
from systems.worldobject import WorldObject
from utility import clamp


class Character(WorldObject):
    
    def __init__(self, name: str, sprite: str, y: int, x: int, 
                 collison: bool = True, health: int = 10, strength: int = 1, speed: int = 1) -> None:

        super().__init__(name, sprite, y, x, collison)
        
        self.health = health
        self.max_health = health
        self.strength = strength 
        self.speed = speed
        
        self.facing = 'north'   


    def will_collide(self, world: list[list]):

        target: Character = self.get_target(world)
        
        if hasattr(target, "collision") and target.collision == False:
            return False
        
        else:
            return True
        
    
    def get_target(self, world: list[list]) -> WorldObject:

        step: dict = self.direction_calc(self.facing)

        try:
            target: WorldObject = world[self.y + step["y-axis"]][self.x + step["x-axis"]]
        
        except IndexError:
            return
        
        return target
    
    
    def movement(self, direction: str, world: list[list]):

        self.facing = direction

        for _ in range(self.speed):

            step = self.direction_calc(direction)
            
            if not self.will_collide(world):
            
                world[self.y][self.x] = self.ground

                self.y += step["y-axis"]
                self.x += step["x-axis"]
                
                self.ground = world[self.y][self.x]
                
                world[self.y][self.x] = self
    

    def attack(self, target: WorldObject):
        target.health = clamp(target.health - self.strength, target.max_health, 0)


    def update(self, world: list[list]):

        if self.health <= 0:
            self.delete(world)

            
        
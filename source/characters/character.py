
from systems.worldobject import WorldObject, Material
from utility import clamp


class Character(WorldObject):
    
    def __init__(self, name: str, sprite: str, y: int, x: int, material: Material,
                 collison: bool = True, health: int = 10, strength: int = 1, speed: int = 1) -> None:

        super().__init__(name, sprite, y, x, material, collison)
        
        self.health = health
        self.base_health = health
        
        self.strength = strength 
        self.base_strength = strength

        self.speed = speed
        self.base_speed = speed

        self.alive = True

        #self.reversed_sprite = self.sprite[::-1]
        
        self.facing = 'north'   

    def get_target(self, world: list[list]) -> WorldObject:

        step: dict = self.direction_calc(self.facing)

        try:
            target: WorldObject = world[self.y + step["y-axis"]][self.x + step["x-axis"]]
        
        except IndexError:
            return
        
        return target
    

    def will_collide(self, world: list[list]):

        target: WorldObject = self.get_target(world)

        if target is None:
            return True
        
        return target.collision
    

    def movement(self, direction: str, world: list[list]):
    
        self.facing = direction

        for _ in range(self.speed):

            step = self.direction_calc(direction)
            
            if not self.will_collide(world):
            
                world[self.y][self.x] = self.behind

                self.y += step["y-axis"]
                self.x += step["x-axis"]
                
                self.behind = world[self.y][self.x]
                
                world[self.y][self.x] = self

    
    def take_damage(self, damage: int):
        self.health = clamp(self.health - damage, min=0)
    
    def heal(self, regeneration: int):
        self.health = clamp(self.health + regeneration, max=self.base_health)

    def update(self, world: list[list]):

        super().update(world)

        if self.health <= 0:
            self.delete(world)

            
        
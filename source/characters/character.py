
from tkinter import W
from systems.worldobject import WorldObject, ObjectCategory

class Character(WorldObject):
    
    def __init__(self, name: str, sprite: str, y: int, x: int, category: ObjectCategory, 
                 collison: bool = True,  health: int = 100, strength: int = 1, speed: int = 1) -> None:

        super().__init__(name, sprite, y, x, category, collison)
        
        self. health = health
        self.strength = strength 
        self.speed = speed
        
        self.facing = 'north'   


    def direction_calc(self, direction: str):
        
        step: dict = {"y-axis": 0, "x-axis": 0}
        
        match direction:
            
            case 'north':
                step["y-axis"] -= 1
            
            case 'south':
                step["y-axis"] += 1
            
            case 'east':
                step["x-axis"] += 1
            
            case 'west':
                step["x-axis"] -= 1
        
        return step
            

    def will_collide(self, step: dict, world: list):
        
        try:
            if world[self.y + step["y-axis"]][self.x + step["x-axis"]].collision == False:
                return False
            
            else:
                return True
        
        except IndexError:
            return True
    
    
    def movement(self, direction: str, world: list):

        for _ in range(self.speed):

            step = self.direction_calc(direction)
            
            if not self.will_collide(step, world):
            
                world[self.y][self.x] = self.ground

                self.y += step["y-axis"]
                self.x += step["x-axis"]
                
                self.ground = world[self.y][self.x]
                
                world[self.y][self.x] = self
    

    def react(self, actor, world: list):
        pass


    def status_check(self):

        if self.health <= 0:
            return "dead"
        
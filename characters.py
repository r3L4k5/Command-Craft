
from enviorment import Grass


class Stats():
    def __init__(self, health = 100, strength = 1, speed = 1) -> None:
        
        self.health: health
        self.strength: strength
        self.speed: speed


class Character():
    
    def __init__(self, step: list[int] = [], stats = Stats()) -> None:
        
        self.stats = stats
        self.step = step
        self.floor = Grass()
    

    def will_collide(self, step, world):
        
        try:
            if world[self.y + step[0]][self.x + step[1]].collision == False:
                return False
            
            else:
                return True
        
        except IndexError:
            return True
        

    def movement(self, direction, world):
        
        step = [0,0]
        
        match direction:
            
            case "w":
                step[0] -= 1
            
            case "s":
                step[0] += 1
            
            case "d":
                step[1] += 1
            
            case "a":
                step[1] -= 1

        if not Character.will_collide(self, step, world):
        
            world[self.y][self.x] = self.floor

            self.y += step[0]
            self.x += step[1]
            
            self.floor = world[self.y][self.x]
            
            world[self.y][self.x] = self
        
        else:
            print("Can't")
        
        return world








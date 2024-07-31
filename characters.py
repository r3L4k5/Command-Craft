
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
    

    def will_collide(self, map):
        try:
            if map[self.pos[0] + self.step[0]][self.pos[1] + self.step[1]].collision == False:
                return False
            
            else:
                return True
        
        except:
            return True
        

    def movement(self, direction, map):
        
        self.step = [0,0]
        
        match direction:
            
            case "w":
                self.step[0] -= 1
            
            case "s":
                self.step[0] += 1
            
            case "d":
                self.step[1] += 1
            
            case "a":
                self.step[1] -= 1

        if not Character.will_collide(self, map):

            map[self.pos[0]][self.pos[1]] = self.floor

            self.pos[0] += self.step[0]
            self.pos[1] += self.step[1]
            
            map[self.pos[0]][self.pos[1]] = self
        
        else:
            print("Can't")
        
        return map


    def spawn(self, spawn_point, map):
        
        if map[spawn_point[0]][spawn_point[1]].collision == False:
            
            self.pos = spawn_point
            map[spawn_point[0]][spawn_point[1]] = self
        
        else:
            print("Can't")






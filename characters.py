
from enviorment import Grass

class Stats():
    def __init__(self, health = 100, strength = 1, speed = 1) -> None:
        
        self.health: health
        self.strength: strength
        self.speed: speed


class Character():
    
    def __init__(self, direction: list[int] = [], stats = Stats()) -> None:
        
        self.stats = stats
        self.direction = direction
        self.floor = Grass()
    

    def will_collide(target_pos, map):
        
        if map[target_pos[0]][target_pos[1]].collision == False:
            return False
        
        else:
            return True
        

    def movement(self, direction, map):
        
        destination = self.position
        
        match direction:
            
            case "up":
                destination[0] -= 1
            
            case "down":
                destination[0] += 1
            
            case "right":
                destination[1] += 1
            
            case "left":
                destination[1] -= 1

        if not Character.will_collide(destination, map):
            
            map[self.position[0]][self.position[1]] = self.floor
    
            self.floor = map[destination[0]][destination[1]]
            
            self.position = destination
            
            map[destination[0]][destination[1]] = self
        
        else:
            print("Can't")
        
        return map


    """def spawn(self, spawn_point, map):
        
        if map[spawn_point[0]][spawn_point[1]].collision == False:
            
            self.position = spawn_point
            map[spawn_point[0]][spawn_point[1]] = self
        
        else:
            print("Can't")"""






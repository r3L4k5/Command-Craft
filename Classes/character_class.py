
class Stats():
    
    def __init__(self, health = 100, strength = 1, speed = 1) -> None:
        
        self.health = health
        self.strength =  strength
        self.speed =  speed


class Character():
    
    def __init__(self, stats = Stats()) -> None:
        
        self.stats = stats
        self.facing = 'w'
        

    def direction_calc(self, direction, distance: int = 1):
        
        step = [0,0]
        
        match direction:
            
            case 'w':
                step[0] -= distance
            
            case 's':
                step[0] += distance
            
            case 'd':
                step[1] += distance
            
            case 'a':
                step[1] -= distance
        
        return step
            

    def will_collide(self, step, world):
        
        try:
            if world[self.y + step[0]][self.x + step[1]].collision == False:
                return False
            
            else:
                return True
        
        except IndexError:
            return True
    
    
    def movement(self, direction, world):
        
        step = self.direction_calc(direction)
        
        if not self.will_collide(step, world):
        
            world[self.y][self.x] = self.ground

            self.y += step[0]
            self.x += step[1]
            
            self.ground = world[self.y][self.x]
            
            world[self.y][self.x] = self
        










class Stats():
    
    def __init__(self, health = 100, strength = 1, speed = 1) -> None:
        
        self.health = health
        self.strength =  strength
        self.speed =  speed


class Character():
    
    def __init__(self, health: int = 100, strength: int = 1, speed: int = 1) -> None:
        
        self. health = health
        self.strength = strength 
        self.speed = speed
        
        self.facing = 'north'   


    def direction_calc(self, direction):
        
        step = [0,0]
        
        match direction:
            
            case 'north':
                step[0] -= 1
            
            case 'south':
                step[0] += 1
            
            case 'east':
                step[1] += 1
            
            case 'west':
                step[1] -= 1
        
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

        for _ in range(self.speed):

            step = self.direction_calc(direction)
            
            if not self.will_collide(step, world):
            
                world[self.y][self.x] = self.ground

                self.y += step[0]
                self.x += step[1]
                
                self.ground = world[self.y][self.x]
                
                world[self.y][self.x] = self
        









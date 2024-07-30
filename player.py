
from characters import Character
from objects import GameObject, ObjectCategory

class Player(Character, GameObject):
    
    def __init__(self) -> None:
        super(GameObject, self).__init__(" i", [0,20], ObjectCategory.PLAYER, True)
        super().__init__()
        
        self.stats.health = 100
        self.stats.strength = 1
        self.stats.speed = 1


    def movement(self, map):
        
        if map[self.position[0]][self.position[1]].collision == False:
            
            map[self.position[0]][self.position[1]] = self
        
        else:
            print("Can't")
        
        return map

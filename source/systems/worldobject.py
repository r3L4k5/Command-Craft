
from enviorment.ground import Grass
from utility import bold


class WorldObject():
    
    def __init__(self, name: str, sprite: str, y: int, x: int, collision: bool = True) -> None:
        
        self.sprite = sprite
        self.collision = collision
        self.name = name
        
        self.y = y
        self.x = x

        self.ground = Grass(y, x)      

    def __str__(self) -> str:
        return self.sprite
    
    def delete(self, world) -> None:
        
        world[self.y][self.x] = self.ground
        del self

    #Show name for presentation, such as dialogue
    def display_name(self):
        return bold(self.name.capitalize())


    
    


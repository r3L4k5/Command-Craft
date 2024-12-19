
from systems.worldobject import WorldObject, Material
import termcolor as ter


class Grass(WorldObject):

    def __init__(self, y: int, x: int) -> None:
            
        super().__init__("grass", ter.colored(" ;", "light_green"), y, x, Material.PLANT, False)

        self.behind = None
    
    def update(self, world: list[list]):
        
        pass




    



        


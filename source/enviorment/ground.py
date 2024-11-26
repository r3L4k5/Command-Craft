
from systems.worldobject import WorldObject, Material
from termcolor import colored


class Grass(WorldObject):

    def __init__(self, y: int, x: int) -> None:
            
        super().__init__("grass", colored(" ;", "light_green"), y, x, Material.PLANT, False)
    
    





    



        


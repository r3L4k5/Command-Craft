
from systems.worldobject import WorldObject
from termcolor import colored


class Fire(WorldObject):
    
    def __init__(self, y: int, x: int) -> None:

        super().__init__("fire", colored("ww", color= "yellow", on_color="on_red", attrs=["bold", "dark"]), y, x, True)

        self.spreading_timer: int = 5
    

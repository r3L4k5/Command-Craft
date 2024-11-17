
from termcolor import colored


class Grass():
    
    def __init__(self, y: int, x: int) -> None:

        self.sprite = colored(" ;", "light_green")
        self.name = "grass"

        self.y = y
        self.x = x

        self.collision = False

    def __str__(self) -> str:
        return self.sprite

    def update(self, world):
        pass






    



        


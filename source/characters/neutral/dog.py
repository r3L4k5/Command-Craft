
from systems.worldobject import WorldObject
from characters.npc import NPC
from termcolor import colored
from random import choice


class Dog(NPC):

    def __init__(self, y: int, x: int) -> None:

        colors: list = ["white", "black", "brown"]
        sprite: str
        
        match choice(colors):

            case "white":
                sprite = colored(" m", attrs=["bold"])
            
            case "black":
                sprite = colored(" m", "black", attrs=["bold"])
            
            case "brown":
                sprite = colored(" m", "red", attrs=["bold", "dark"])
            
            case "grey":
                sprite = colored(" m", "light_grey", attrs=["bold"])


        super().__init__("dog", sprite, y, x, 5, 1, 1, 3)


    def react(self, actor, world):
        input("Ruff!")

    
    def detection(self, world: list):

        vision_field = self.vision_calc(world)

        for y in range(vision_field["north"], vision_field["south"]):
            for x in range(vision_field["west"], vision_field["east"]):
                
                self.move_toward(world[y][x], world)


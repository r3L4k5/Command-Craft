
from enviorment.ground import Grass
from enum import Enum, auto
from utility import bold


class Material(Enum):
    PLANT = auto(),
    FLESH = auto(),
    MINERAL = auto(),
    MISC = auto()


class WorldObject():
    
    def __init__(self, name: str, sprite: str, y: int, x: int, material: Material, collision: bool = True) -> None:
        
        self.sprite = sprite
        self.collision = collision
        self.name = name
        self.material = material
        
        self.y = y
        self.x = x

        self.ground = Grass(y, x)      


    def __str__(self) -> str:
        return self.sprite
    

    def delete(self, world: list[list]) -> None:

        world[self.y][self.x] = self.ground
        del self


    def update(self, world: list[list]):

        if isinstance(self.ground, WorldObject):
            self.ground.update(world)
            

    #Show name for presentation, such as dialogues
    def display_name(self):
        return bold(self.name.capitalize())


    def direction_calc(self, direction: str | None = None, increment: int = 1):
    
        step: dict = {"y-axis": 0, "x-axis": 0}

        match direction:

            case 'north':
                step["y-axis"] -= increment

            case 'south':
                step["y-axis"] += increment

            case 'east':
                step["x-axis"] += increment

            case 'west':
                step["x-axis"] -= increment

        return step
    

    def get_target(self, world: list[list], direction: str| None = None) -> object:

        step: dict = self.direction_calc(direction)

        try:
            target: WorldObject = world[self.y + step["y-axis"]][self.x + step["x-axis"]]
        
        except IndexError:
            return
        
        return target
    

    def interacted(self, actor: object, world: list[list]):
        pass
        


    
    


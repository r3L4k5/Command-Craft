
from systems.worldobject import WorldObject


class Tile():

    def __init__(self, ground: WorldObject, surface: WorldObject | None = None, air: WorldObject | None = None) -> None:
        
        self.ground = ground
        self.surface = surface
        self.air = air


class World():

    def __init__(self, size_y: int, size_x: int) -> None:
        
        self.map = self.create_map()

        self.size_y = size_y
        self.size_x = size_x


    def create_map(self):
        
        pass
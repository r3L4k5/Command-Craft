
from characters import Character, Stats
from objects import GameObject, ObjectCategory


class Player(GameObject, Character):
    
    def __init__(self) -> None:
        
        super().__init__(" i", [], ObjectCategory.PLAYER)
        Character.__init__(self, stats= Stats())
    
    
        
    
    
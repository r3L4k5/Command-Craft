
from characters import Character, Stats
from objects import GameObject, ObjectCategory


controls = {
    "movement": ["w", "s", "a", "d"]
}


class Player(GameObject, Character):
    
    def __init__(self) -> None:
        
        super().__init__(" i", [], ObjectCategory.PLAYER)
        Character.__init__(self, stats= Stats())
    
    def input_handler(self, map):

        player_input = list(input(" \n\n  Input controll: "))

        for inputs in player_input:
            
            if inputs in controls["movement"]:
            
                self.movement(inputs, map)
        
    
        
    
    
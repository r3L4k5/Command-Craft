
from characters import Character, Stats
from objects import GameObject, ObjectCategory


controls = {
    "movement": ["w", "s", "a", "d"],
    "interact": "e"
}


class Player(GameObject, Character):
    
    def __init__(self, world) -> None:
        
        super().__init__(" i", 0, 10, ObjectCategory.PLAYER)
        Character.__init__(self, stats= Stats())

        world[self.y][self.x] = self
    

    def input_handler(self, world):

        player_input = list(input(" \n\n  Input controll: "))

        for inputs in player_input:
            
            if inputs in controls["movement"]:
            
                self.movement(inputs, world)
            
            elif inputs in controls["interact"]:
                pass

        
    
        
    
    
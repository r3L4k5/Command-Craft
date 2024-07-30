

class CharacterStats():
    def __init__(self) -> None:
        
        self.health: int
        self.strength: int 
        self.speed: int 


class Character():
    
    def __init__(self, target_position: list[int] = [], stats = CharacterStats()) -> None:
        
        self.stats = stats
        self.target_position = target_position




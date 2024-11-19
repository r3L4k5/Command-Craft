

class Item():
    
    def __init__(self, name: str, sprite: str, amount: int = 1) -> None:
        
        self.name: str = name
        self.sprite: str = sprite
        self.amount: int = amount
    
    def effect(self, world, player, target):
        pass
    
    def __str__(self) -> str:
        return f"{self.sprite} {self.name.capitalize()} x{self.amount}"
    
    def __eq__(self, value: object) -> bool:
        return type(self) == type(value)

    



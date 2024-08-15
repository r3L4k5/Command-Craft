
class Item():
    
    def __init__(self, name: str, sprite: str, amount: int) -> None:
        
        self.name: str = name
        self.sprite: str = sprite
        self.amount: str = amount
    
    def __str__(self) -> str:
        return self.sprite


    


class Item():
    
    def __init__(self, name: str, sprite: str, amount: int) -> None:
        
        self.name: str = name
        self.sprite: str = sprite
        self.amount: str = amount

        self.recipe = None
    
    def __str__(self) -> str:
        return self.sprite
    
    def __eq__(self, value: object) -> bool:
        return type(self) == type(value)
    

    

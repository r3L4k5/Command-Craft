
from systems.worldobject import WorldObject

class Item():
    
    def __init__(self, name: str, sprite: str, use_in_inventory: bool, amount: int = 1) -> None:
        
        self.name: str = name
        self.sprite: str = sprite
        self.amount: int = amount
        self.use_in_inventory: bool = use_in_inventory
    
    def effect(self, world: list[list], actor: WorldObject, target: WorldObject):
        pass
    
    def __str__(self) -> str:
        return f"{self.sprite} {self.name.capitalize()} x{self.amount}"
    
    def __eq__(self, value: object) -> bool:
        return type(self) == type(value)

    def delete(self, storage: object, equip = None):

        if self == equip:
            equip = None
            
        else:
            storage.remove_item(self)
        

    



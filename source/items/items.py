
from systems.worldobject import WorldObject


class Item():
    
    def __init__(self, name: str, sprite: str, amount: int = 1) -> None:
        
        self.name: str = name
        self.sprite: str = sprite
        self.amount: int = amount
    
    #In effect when interacting while having item equipped
    def equipped_effect(self, world: list[list], actor: WorldObject, target: WorldObject) -> str:
        
        return "No effect"
    
    #In effect every game loop while having the item equipped
    def passive_effect(self, world: list[list], actor: WorldObject, target: WorldObject) -> str:
        
        return "No effect"

    #In effect when item used in inventory
    def inventory_effect(self, world: list[list], actor: WorldObject, target: WorldObject) -> str:

        return "No effect"
        
    def __str__(self) -> str:
        return f"{self.sprite} {self.name.capitalize()} x{self.amount}"
    
    def __eq__(self, value: object) -> bool:
        return type(self) == type(value)

    def delete(self, storage: object, equip = None):

        if self == equip:
            equip = None
            
        else:
            storage.remove_item(self)
        


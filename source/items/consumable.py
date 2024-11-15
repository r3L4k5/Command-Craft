
from items.items import Item, Material
from characters.character import Character


class Consumable(Item):

    def __init__(self, name: str, sprite: str, can_cook: bool, amount: int = 1) -> None:

        super().__init__(name, sprite, Material.NONE, amount)

        self.can_cook = can_cook
        self.cooked = False

    def effect(self, player: Character):

        if self.cooked:
            player.health += player.max_health * 0.2
        else:
            player.health += player.max_health * 0.1 
        
        del self
    


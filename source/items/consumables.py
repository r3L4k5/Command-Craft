
from items.items import Item, Material
from characters.character import Character
from termcolor import colored
from random import randint


class Consumable(Item):

    def __init__(self, name: str, sprite: str, can_cook: bool, amount: int = 1) -> None:

        super().__init__(name, sprite, Material.NONE, amount)

        self.can_cook = can_cook
        self.cooked = False

    def cook(self):
        if not self.can_cook:
            return

    def effect(self, player: Character):

        if self.cooked:
            player.health += player.max_health * 0.2
        else:
            player.health += player.max_health * 0.1 
        
        del self
        

class Meat(Consumable):

    def  __init__(self, amount: int = 1) -> None:

        super().__init__("meat", colored("||", on_color="on_red", attrs=["bold"]), True, amount)
    
    def effect(self, player: Character):
        
        if self.cooked:
            player.health += player.max_health * 0.2

        else:
            random_effect: int = randint(1, 2)

            if random_effect == 1:
                player.health += player.max_health * 0.1 
            
            else:
                player.health -= player.max_health * 0.1
        
        del self

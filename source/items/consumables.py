
from items.items import Item
from characters.character import Character
from termcolor import colored
from random import randint


class Consumable(Item):

    def __init__(self, name: str, sprite: str, can_cook: bool, amount: int = 1) -> None:

        super().__init__(name, sprite, True, amount)

        self.can_cook = can_cook
        self.cooked = False

    def cook(self):

        if not self.can_cook:
            return

    def effect(self, world: list[list], player: Character):
        pass
        

class Meat(Consumable):

    def  __init__(self, amount: int = 1) -> None:

        super().__init__("meat", colored("||", on_color="on_red", attrs=["bold"]), True, amount)

    
    def effect(self, world: list[list], actor: Character, target = None):
        
        if self.cooked:
            actor.health += actor.max_health * 0.2

        else:
            random_effect: int = randint(1, 2)

            if random_effect == 1:
                actor.health += actor.max_health * 0.1 
            
            else:
                actor.health -= actor.max_health * 0.1
        

        if self == actor.equipped:

            actor.equipped = None

        else:
            actor.inventory.remove_item(self)


from items.items import Item
from characters.character import Character
import termcolor as ter
from random import randint


class Consumable(Item):

    def __init__(self, name: str, sprite: str, can_cook: bool, amount: int = 1) -> None:

        super().__init__(name, sprite, amount)

        self.can_cook = can_cook
        self.cooked = False

    def cook(self):

        if self.can_cook:
            self.cooked = True
    

class Meat(Consumable):

    def  __init__(self, amount: int = 1) -> None:

        super().__init__("meat", ter.colored("||", on_color="on_red", attrs=["bold"]), True, amount)

    
    def inventory_effect(self, world: list[list], actor: Character, target = None):
        
        if self.cooked:
            actor.heal(actor.base_health * 0.2)

        else:
            random_effect: int = randint(1, 2)

            if random_effect == 1:
                actor.heal(actor.base_health * 0.1)
            
            else:
                actor.take_damage(actor.base_health * 0.1)
        

        self.delete(actor.inventory, actor.equipped)


class Fruit(Consumable):

    def __init__(self, amount = 1):

        super().__init__("fruit", ter.colored("(", color="red", attrs=["bold"] ) 
                        + ter.colored("`", color="green", attrs=["bold"]) + ter.colored(")", color="red", attrs=["bold"]), False, amount)


    def inventory_effect(self, world: list[list], actor: Character, target = None):

        actor.heal(1)

        self.delete(actor.inventory, actor.equipped)
        

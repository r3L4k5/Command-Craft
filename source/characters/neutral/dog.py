
from items.item_access import get_item
from characters.npc import NPC
from characters.character import Character


class Dog(NPC):

    def __init__(self, y: int, x: int) -> None:

        super().__init__("dog", " m", y, x, health= 6, strength= 1, speed= 1, vision= 6, loot= [get_item("meat")])
    
    
    def react(self, actor: Character, world: list[list], friendly: bool):

        if friendly:
            input(f"\n{self.display_name()}: Ruff!")

        else:
            input(f"\n{self.display_name()}: Grrh! [Attcking]")
            self.attack(actor)






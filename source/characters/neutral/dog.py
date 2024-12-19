
from items.item_access import get_item
from characters.npc import NPC
from characters.character import Character
from systems.worldobject import Material


class Dog(NPC):

    def __init__(self, y: int, x: int) -> None:

        super().__init__("dog", "*m", y, x, Material.FLESH, health = 6, strength= 1, speed= 1, vision= 6,
                        loot= [get_item("meat"), get_item("leather")])
        
        self.debug: str = ""
    
    
    def interacted(self, actor: Character, world: list[list], friendly: bool = True):

        if friendly:
            input(f"\n{self.display_name()}: Ruff!")

        else:
            input(f"\n{self.display_name()}: Grrh! [Attcking]")

            self.take_damage(actor.strength)
            actor.take_damage(self.strength)

    
    def update(self, world):

        if len(self.debug) > 0:
            input(self.debug)

        return super().update(world)
    



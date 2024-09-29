
import  items.resources as res
import  items.craftable as too 

from copy import deepcopy 

class MaterialColor():

    def __init__(self, color: str, brightness: str ) -> None:
        
        self.color: str = color
        self.brightness: str = brightness

    def __eq__(self, value: object) -> bool:

        if self.color == value.color and self.brightness == value.brightness:
            return True

WOOD = MaterialColor("red", "dark")
STONE = MaterialColor("grey", "dark")


def get_item(item_name: str) -> object:

    return deepcopy(item_access[item_name])

item_access = {
    "wood" : res.Wood(1),
    "stone": res.Stone(1),

    "woodensword": too.Sword(WOOD, {"wood": 4}, 2, 10),
    "stonesword": too.Sword(STONE, {"stone": 3, "wood": 1}, 5, 20)
}
 
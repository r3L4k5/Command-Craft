
import items.resources as res
import items.tools as too

from items.items import Material as mat
from items.items import Item
from copy import deepcopy 


def get_item(item_name: str) -> object:

    return deepcopy(item_access[item_name])


item_access: dict = {

    "wood" : res.Wood(1),
    "stone": res.Stone(1),

    "woodensword": too.Sword(mat.WOOD, {"wood": 4}, 10, 1.5),
    "stonesword": too.Sword(mat.STONE, {"stone": 3, "wood": 1}, 20, 3),

    "woodenaxe": too.Axe(mat.WOOD, {"wood": 4}, 10, 1.5),
    "stoneaxe": too.Axe(mat.STONE, {"stone": 3, "wood": 1}, 20, 3),

    "woodenpickaxe": too.Pickaxe(mat.WOOD, {"wood": 4}, 10, 1.5),
    "stonepickaxe": too.Pickaxe(mat.STONE, {"stone": 3, "wood": 1}, 20, 3),
}
 
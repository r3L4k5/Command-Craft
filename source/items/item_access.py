
import  items.resources as res
import  items.tools as too 

from copy import deepcopy 


def get_item(item_name: str) -> object:

    return deepcopy(item_access[item_name])

item_access = {
    "wood" : res.Wood(1),
    "stone": res.Stone(1),

    "woodensword": too.Sword("wood", {"wood": 4}, 10, 2),
    "stonesword": too.Sword("stone", {"stone": 3, "wood": 1}, 20, 5),

    "woodenaxe": too.Axe("wood", {"wood": 3, "stone": 1}, 10, 2),
    "stoneaxe": too.Axe("stone", {"stone": 3, "wood": 1}, 20, 5),
}
 
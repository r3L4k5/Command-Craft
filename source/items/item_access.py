
import items.resources as res
import items.tools as too
import items.consumables as con
import items.supplies as sup

from items.items import Item
from copy import deepcopy 


def get_item(item_name: str) -> object:

    return deepcopy(item_access[item_name])


item_access: dict[str:Item] = {

    #Resources
    "wood": res.Wood(),
    "stone": res.Stone(),
    "coal": res.Coal(),

    #Tools
    "woodensword": too.Sword(too.Resource.WOOD, {"wood": 4}, 50, 2),
    "stonesword": too.Sword(too.Resource.STONE, {"stone": 3, "wood": 1}, 100, 4),

    "woodenaxe": too.Axe(too.Resource.WOOD, {"wood": 4}, 50, 2),
    "stoneaxe": too.Axe(too.Resource.STONE, {"stone": 3, "wood": 1}, 100, 4),

    "woodenpickaxe": too.Pickaxe(too.Resource.WOOD, {"wood": 4}, 50, 2),
    "stonepickaxe": too.Pickaxe(too.Resource.STONE, {"stone": 3, "wood": 1}, 100, 4),

    #Consumables
    "meat": con.Meat(),

    #Supply
    "torch": sup.Torch(),
}
 
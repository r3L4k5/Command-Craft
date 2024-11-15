
import items.resources as res
import items.tools as too
import items.consumable as con

from items.items import Material as mat
from items.items import Item
from copy import deepcopy 
from termcolor import colored


def get_item(item_name: str) -> object:

    return deepcopy(item_access[item_name])


item_access: dict[str:Item] = {

    #Resources
    "wood": res.Wood(1),
    "stone": res.Stone(1),

    #Tools
    "woodensword": too.Sword(mat.WOOD, {"wood": 4}, 10, 2),
    "stonesword": too.Sword(mat.STONE, {"stone": 3, "wood": 1}, 20, 4),

    "woodenaxe": too.Axe(mat.WOOD, {"wood": 4}, 10, 2),
    "stoneaxe": too.Axe(mat.STONE, {"stone": 3, "wood": 1}, 20, 4),

    "woodenpickaxe": too.Pickaxe(mat.WOOD, {"wood": 4}, 10, 2),
    "stonepickaxe": too.Pickaxe(mat.STONE, {"stone": 3, "wood": 1}, 20, 4),

    #Consumables
    "meat": con.Consumable("meat", colored("||", on_color="on_red", attrs=["bold"]), True)
}
 
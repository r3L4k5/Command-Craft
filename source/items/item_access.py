
import items.resources as res
import items.tools as too
import items.consumables as con
import items.supplies as sup


from items.items import Material as mat
from items.items import Item
from copy import deepcopy 
from termcolor import colored


def get_item(item_name: str) -> object:

    return deepcopy(item_access[item_name])


item_access: dict[str:Item] = {

    #Resources
    "wood": res.Wood(),
    "stone": res.Stone(),
    "coal": res.Coal(),

    #Tools
    "woodensword": too.Sword(mat.WOOD, {"wood": 4}, 50, 2),
    "stonesword": too.Sword(mat.MINERAL, {"stone": 3, "wood": 1}, 100, 4),

    "woodenaxe": too.Axe(mat.WOOD, {"wood": 4}, 50, 2),
    "stoneaxe": too.Axe(mat.MINERAL, {"stone": 3, "wood": 1}, 100, 4),

    "woodenpickaxe": too.Pickaxe(mat.WOOD, {"wood": 4}, 50, 2),
    "stonepickaxe": too.Pickaxe(mat.MINERAL, {"stone": 3, "wood": 1}, 100, 4),

    #Consumables
    "meat": con.Meat(),

    #Supply
    "torch": sup.Torch(),
}
 
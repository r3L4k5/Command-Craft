
import items.item_category.resources as res
import items.item_category.tools as too
import items.item_category.consumables as con
import items.item_category.supplies as sup

from items.items import Item
from copy import deepcopy 




def get_item(item_name: str, amount: int = 1) -> object:
    input(get_item.counter)
    get_item.counter += 1
    new_item: Item = deepcopy(item_access[item_name])
    new_item.amount = amount

    return new_item

get_item.counter = 0

item_access: dict[str:Item] = {

    #Resources
    "wood": res.Wood(),
    "stone": res.Stone(),
    "coal": res.Coal(),
    "leather": res.Leather(),

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
    "shoes": sup.Shoes(),
}
 

import materials.items.resources as res
import materials.items.tools as too 

from enum import Enum

class Material(Enum):
    WOOD = {"color": "red", "attrs": ["bold", "dark"]}
    STONE = {"color": "grey", "attrs": ["bold", "dark"]}

resource_dict = {
    "Wood": res.Wood(),
    "Stone": res.Stone(),
}

craftable_dict = {
    "WoodenSword": too.Sword(Material.WOOD)
}
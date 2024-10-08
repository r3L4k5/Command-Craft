
import  items. resources as res
import  items. tools as too 


class MaterialColor():

    def __init__(self, color: str, brightness: str ) -> None:
        
        self.color: str = color
        self.brightness: str = brightness

WOOD = MaterialColor("red", "dark")
STONE = MaterialColor("grey", "dark")

craft_dict = {
    "woodensword": too.Sword(WOOD, {"wood": 3}, 2, 10),
    "stonesword": too.Sword(STONE, {"stone": 3}, 5, 20)
}

resource_dict = {
    "wood" : res.Wood(),
    "stone": res.Stone()
}
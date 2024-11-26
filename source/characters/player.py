
import utility as uti

from characters.character import Character
from systems.worldobject import WorldObject, Material
from systems.storage import Storage
from items.items import Item

from items.item_access import get_item
from copy import deepcopy
from termcolor import colored


controls = {
    "movement": ['w', 's', 'a', 'd'],
    "inventory": 'q',
    "interact": 'e',
    "use_equip": 'r'
}

facing_directions = {
    'w': "north",
    's': "south",
    'a': "west",
    'd': "east"
}

inventory_modes = {'e' :"craft", 'r': "equip", 't': "use"}


class Player(Character):
    
    def __init__(self, y: int, x: int) -> None:
        
        super().__init__("player", colored(" \"", color="black", on_color="on_white", attrs=["bold"]), y, x, Material.FLESH)
        
        self.input_queue = []

        self.inventory: Storage = Storage(12, 15, name= "Inventory")
        self.equipped: Item | None = None
        
        self.inventory.add_item(get_item("torch"))
        

    def display_health(self) -> str:

        fraction: int = round(self.health / self.max_health, 2)

        bar: str = uti.blank_space(int(10 * fraction))

        color = "on_green"

        if 0.3 < fraction <= 0.66:
            color = "on_yellow"
        
        elif 0 < fraction <= 0.33:
            color = "on_red"

        return f"{uti.bold("Health: ")}{colored(bar, on_color=color, attrs=["bold"])}"


    def display_equip(self) -> str:

        if self.equipped is not None:

            return f"{uti.bold('Equipped:')} [{self.equipped.sprite} {self.equipped.name.capitalize()}]" 
            
        else:
            return uti.bold('Equipped:') + " []"
        

    def display_hud(self) -> None:
        
        print(f" {uti.bold('Facing: ')}{self.facing.capitalize()}", end="     ")

        print(f"{self.display_equip()}", end="     ")

        print(f"{self.display_health()}")


    def equip_item(self, item: str) -> None:

        if item == "none":

            self.inventory.add_item(self.equipped)
            self.equipped = None

            return
        
        to_equip: Item = get_item(item)

        inventory_count: dict = self.inventory.count_items()

        if to_equip.name in inventory_count:

            if self.equipped is not None:
                self.inventory.add_item(self.equipped)

            #Deepcopy so as to not assing the same object in memory
            self.equipped = deepcopy(to_equip)
            self.inventory.remove_item(to_equip) 


    def craft_item(self, item: str) -> None:

        to_craft: Item = get_item(item)
        
        inventory_count = self.inventory.count_items()
        
        consumed_items = []

        if not hasattr(to_craft, "recipe"):
            return

        for ingredient in to_craft.recipe.keys():
            
            if ingredient in inventory_count and inventory_count[ingredient] >= to_craft.recipe[ingredient]:
                
                consumed: Item = get_item(ingredient)
                consumed.amount = to_craft.recipe[ingredient]

                consumed_items.append(consumed)
            
            else:
                return
        
        for consumed in consumed_items:
            
            self.inventory.remove_item(consumed)

        self.inventory.add_item(to_craft)


    def use_item(self, world: list[list], item: str) -> None:

        to_use: Item = get_item(item)

        inventory_count: dict = self.inventory.count_items()

        target: WorldObject = self.get_target(world)

        if not to_use.use_in_inventory:
            return

        elif to_use.name in inventory_count:

            to_use.effect(world, self, target)
        
        elif to_use == self.equipped:

            to_use.effect(world, self, target)

    
    def open_inventory(self, world) -> None:
        
        mode = "craft"

        while True:

            uti.clear()
            
            print(uti.bold(self.inventory.name + ': '), end="\n\n\n")

            print("  " + self.display_equip(), end="   ")
            
            print(f"~{mode}", end="\n\n\n")

            for index, slot in enumerate(self.inventory.slots, 1):

                print(f"  {slot}", end= " ")
                
                uti.row_break(index, 4, 2)

            
            action = uti.standardize(input("\nAction: "))
            
            if action == 'q':
                break

            elif action in inventory_modes.keys():

                mode = inventory_modes[action]
                continue
            
            try:
                match mode:

                    case "craft":
                        self.craft_item(action)

                    case "equip":
                        self.equip_item(action)
                    
                    case "use":
                        self.use_item(world, action)
            
            except KeyError:
                continue


    def interact(self, world: list[list]) -> None:

        target: WorldObject = self.get_target(world)

        if self.equipped is not None:
            self.equipped.effect(world, self, target)
        
        elif isinstance(target, WorldObject):
            target.interacted(self, world)
        

    def update_sprite(self) -> None:

        match self.facing:

            case "east":
                self.sprite = colored(" \"", on_color="on_white", attrs=["bold"])

            case "west":
                self.sprite = colored("\" ", on_color="on_white", attrs=["bold"])
        
        if self.health <= 0:
            self.sprite = colored("**", on_color="on_white", attrs=["bold"])
    

    def input_handler(self, world: list[list]) -> None:
    
        if len(self.input_queue) == 0:

            incoming_input = list(input(uti.standardize(uti.bold("Action: "))))

            if len(incoming_input) == 0: 
                return
            
            self.input_queue.extend(incoming_input)
            

        if self.input_queue[0] in controls["movement"]:
            
            direction: str = facing_directions[self.input_queue[0]]
            
            self.movement(direction, world)
        
        elif self.input_queue[0] == controls["interact"]:
            
            self.interact(world)
        
        elif self.input_queue[0] == controls["inventory"]:
            
            self.open_inventory(world)
        
        self.input_queue.pop(0)
    

    def update(self, world: list[list]):

        super().update(world)

        self.update_sprite()

        if self.health == 0:
            input("Game Over!")
            quit()
 
    


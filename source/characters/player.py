
import utility as uti
import items.tools as too

from characters.character import Character
from systems.worldobject import WorldObject, Material
from systems.storage import Storage
from items.items import Item
from characters.npc import NPC
from enviorment.harvestable import Harvestable
from items.consumables import Consumable

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
    
    def __init__(self, world: list[list]) -> None:
        
        super().__init__("player", colored(" \"", color="black", on_color="on_white", attrs=["bold"]), y= 0, x= 10, material= Material.FLESH)
        
        self.input_queue = []

        self.inventory: Storage = Storage(12, 10, name= "Inventory")
        self.equipped: Item | None = None
        
        world[self.y][self.x] = self  
        

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

        inventory_count: dict = self.count_items()

        if to_equip.name in inventory_count:

            if self.equipped is not None:

                #Sloppy fix, should be worked on in the future
                #Otherwise, it would give back an item with zero amount
                #self.equipped.amount = 1
                self.inventory.add_item(self.equipped)

            #Deepcopy so as to not assing the same object in memory
            self.equipped = deepcopy(to_equip)
            self.inventory.remove_item(to_equip) 
        

    def count_items(self) -> dict:

        item_count = {}
        
        for slot in self.inventory.slots:

            if slot.empty: 
                continue

            elif slot.item.name in item_count:

                item_count[slot.item.name] += slot.item.amount

            else:
                item_count[slot.item.name] = slot.item.amount
        
        return item_count


    def craft_item(self, item: str) -> None:

        to_craft: Item = get_item(item)
        
        inventory_count = self.count_items()
        
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


    def use_item(self, item: str) -> None:

        to_use: Item = get_item(item)

        inventory_count: dict = self.count_items()

        if not isinstance(to_use, Consumable):
            return

        elif to_use.name in inventory_count:

            to_use.effect(self)
            self.inventory.remove_item(to_use)
        
        elif to_use == self.equipped:

            to_use.effect(self)
            self.equipped = None
        
    
    def open_inventory(self) -> None:
        
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
                        self.use_item(action)
            
            except KeyError:
                continue


    def interact(self, world: list[list]) -> None:

        if self.equipped is not None:
            self.equipped.effect()

        '''if "supplies" in getattr(self.equipped, "__module__", []):
            self.equipped.effect(self, world)
        
        elif isinstance(self.equipped, Consumable):
            self.equipped.effect(self)
        

        target: WorldObject = self.get_target(world)
        
        if isinstance(target, Harvestable):
            target.harvest(self, world)
        
        elif isinstance(target, NPC):

            if isinstance(self.equipped, too.Sword):
                self.attack(target, world)
            
            else:
                target.react(self, world, True)'''
        
        
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

            incoming_input = list(input(uti.bold("Action: ")).strip())

            if len(incoming_input) == 0: 
                return
            
            self.input_queue.extend(incoming_input)
            

        if self.input_queue[0] in controls["movement"]:
            
            direction: str = facing_directions[self.input_queue[0]]
            
            self.movement(direction, world)
        
        elif self.input_queue[0] == controls["interact"]:
            
            self.interact(world)
        
        elif self.input_queue[0] == controls["inventory"]:
            
            self.open_inventory()
        
        self.input_queue.pop(0)
    

    def attack(self, target: NPC, world: list[list]):

        total_strength = self.strength * self.equipped.effect(self)
        target.health = uti.clamp(target.health - total_strength, target.max_health, 0)

        if target.health == 0 and target.loot is not None:

            for item in target.loot:
                self.inventory.add_item(item)
        
        else:
            target.react(self, world, False)
    

    def update(self, world: list[list]):

        super().update(world)
        self.update_sprite()

        if self.health == 0:
            input("Game Over!")
            quit()
 
    


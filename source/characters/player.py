
from math import e
import utility as uti
import items.resources as res
import items.tools as too


from characters.character import Character
from systems.worldobject import WorldObject, ObjectCategory
from systems.storage import Storage
from items.items import Item
from items.item_access import get_item


controls = {
    "movement": ['w', 's', 'a', 'd'],
    "inventory": 'q',
    "interact": 'e'
}

facing_directions = {
    'w': "north",
    's': "south",
    'a': "west",
    'd': "east"
}


class Player(Character):
    
    def __init__(self, world: list) -> None:
        
        super().__init__("player", " i", 0, 10, ObjectCategory.PLAYER)

        self.input_queue = []

        self.inventory: Storage = Storage(12, 10, "-Empty-", "Inventory")
        self.equipped: Item | None = None

        #For devolopement, so no need to harvest 
        #resources to craft
        self.inventory.add_item(res.Wood(10))
        self.inventory.add_item(res.Stone(10))
        
        world[self.y][self.x] = self   

    
    def display_equip(self) -> str:

        if self.equipped is not None:

            return f"{uti.bold('Equipped:')} [{self.equipped} {self.equipped.name.capitalize()}]" 
            
        else:
            return uti.bold('Equipped:') + " []"


    def display_hud(self) -> None:
        
        print(f" {uti.bold('Facing: ')}{self.facing.capitalize()}", end="     ")

        print(f"{self.display_equip()}", end="     ")

        print(f"{uti.bold('Health: ')}{self.health}")


    def equip_item(self, item: str) -> None:
        
        to_equip: Item = get_item(item)

        inventory_count: dict = self.count_items()

        if to_equip.name in inventory_count:

            if self.equipped is not None:

                #Sloppy fix, should be worked on in the future
                #Otherwise, it would give back an item with zero amount
                #self.equipped.amount = 1
                self.inventory.add_item(self.equipped)
            
            self.equipped = to_equip
            self.inventory.remove_item(to_equip)
        

    def count_items(self) -> dict:

        item_count = {}
        
        for slot in self.inventory.slots:

            if slot.empty: continue

            elif slot.item.name in item_count:

                item_count[slot.item.name] += slot.amount

            else:
                item_count[slot.item.name] = slot.amount
        
        return item_count


    def craft_item(self, item: str) -> None:

        to_craft: Item = get_item(item)
        
        inventory_count = self.count_items()
        
        consumed_items = []

        for ingredient in to_craft.recipe.keys():
            
            if ingredient in inventory_count and inventory_count[ingredient] >= to_craft.recipe[ingredient]:
                
                resource: Item = get_item(ingredient)
                resource.amount = to_craft.recipe[ingredient]

                consumed_items.append(resource)
                 
            else:
                return
        
        for consumed in consumed_items:
            
            self.inventory.remove_item(consumed)

        self.inventory.add_item(to_craft)

    
    def open_inventory(self) -> None:
        
        mode = "craft"

        while True:

            uti.clear()
            
            print(uti.bold(self.inventory.name + ': '), end="\n\n\n")

            print("  " + self.display_equip(), end="   ")
            
            print(f"~{mode}", end="\n\n\n")


            for index, slot in enumerate(self.inventory.slots, 1):

                if slot.empty: 
                    print(f"  [{slot.item}]", end= " ")
                
                else:
                    print(f"  [{str(slot.item)} {slot.item.name.capitalize()} x{slot.amount}]", end= " ")
                
                uti.row_break(index, 4, 2)

            
            action = uti.del_space(input("\nAction: ")).lower()
            
            match action:
                
                case 'q': 
                    return

                case 'e':
                    
                    if mode == "craft": 
                        mode = "equip"
                    else:
                        mode = "craft"
                    
                    continue
            
            try:
                match mode:

                    case "craft":
                        self.craft_item(action)

                    case "equip":
                        self.equip_item(action)
            
            except KeyError:
                continue
        
    
    def interact(self, world: list) -> None:
        
        step: dict = self.direction_calc(self.facing)

        try:
            target: WorldObject = world[self.y + step["y-axis"]][self.x + step["x-axis"]]
        
        except IndexError:
            return

        if target.collision == False:
            return

        match target.category:

            case ObjectCategory.HARVESTABLE:
                target.harvest(self, world)

            case ObjectCategory.NPC:

                if isinstance(self.equipped, too.Sword):

                    self.attack(target, world)
                    return
                
                target.react(self, world)
    
    
    def input_handler(self, world: list) -> None:
    
        if len(self.input_queue) == 0:

            incoming_input = list(input(" Action: ").strip())

            if len(incoming_input) == 0: 
                return
            
            self.input_queue.extend(incoming_input)
            

        if self.input_queue[0] in controls["movement"]:
            
            self.facing = facing_directions[self.input_queue[0]]
            
            self.movement(self.facing, world)
        
        elif self.input_queue[0] == controls["interact"]:
            
            self.interact(world)
        
        elif self.input_queue[0] == controls["inventory"]:
            
            self.open_inventory()
        
        else:
            pass

        self.input_queue.pop(0)
    

    def attack(self, target: Character, world):

        total_strength = self.strength * self.equipped.effect()
        target.take_damage(total_strength, world)


    def update_player(self, world: list) -> None:

        self.input_handler(world)
        self.display_hud()

    


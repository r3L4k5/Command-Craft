
import utility as uti
import items.item_dict as item_dict

from characters.character_class import Character
from misc_classes.object_class import WorldObject, Category
from misc_classes.storage_class import Storage
from items.item_class import Item


controls = {
    "movement": ['w', 's', 'a', 'd'],
    "inventory": 'q',
    "interact": 'e'
}

facing_directions = {
    'w': "North",
    's': "South",
    'a': "West",
    'd': "East"
}


class Player(WorldObject, Character):
    
    def __init__(self, world: list) -> None:
        
        super().__init__(" i", 0, 10, Category.PLAYER)
        Character.__init__(self)

        self.input_queue = []
        self.inventory = Storage(12, 10, "-Empty-", "Inventory")
        
        self.equipped: Item

        #For devolopement, so no need to harvest resources
        #self.inventory.add_item(res.Wood(10))
        #self.inventory.add_item(res.Stone(10))
        
        world[self.y][self.x] = self

    
    def display_hud(self):
        
        print(f" {uti.bold('Facing: ')}{facing_directions[self.facing]}", end="")
        
        print(f"{uti.bold('Health: '):>50}{self.health}")


    def equip_item(self, item: str):
        
        to_equip: Item = item_dict.resource_dict[item]

        inventory_count = self.count_items()

        if to_equip.name in inventory_count:
            
            self.inventory.remove_item(to_equip, "-Equipped-")
            self.equipped = to_equip
            self.sprite = to_equip.sprite + self.sprite


    def count_items(self):

        item_count = {}
        
        for slot in self.inventory.slots:

            if slot.empty: continue

            elif slot.item.name in item_count:

                item_count[slot.item.name] += slot.amount

            else:
                item_count[slot.item.name] = slot.amount
        
        return item_count


    def craft_item(self, item: str):

        to_craft: Item = item_dict.craft_dict[item]
        
        inventory_count = self.count_items()
        
        consumed_items = []

        for ingredient in to_craft.recipe.keys():
            
            if ingredient in inventory_count and inventory_count[ingredient] >= to_craft.recipe[ingredient]:
                
                resource = item_dict.resource_dict[ingredient]
                resource.amount = to_craft.recipe[ingredient]

                consumed_items.append(resource)
                 
            else:
                return
        
        for consumed in consumed_items:
            
            self.inventory.remove_item(consumed)

        self.inventory.add_item(to_craft)

    
    def open_inventory(self):
        
        mode = "craft"

        while True:

            uti.clear()
            
            print(uti.bold(self.inventory.name + ': '), end="\n\n")

            for index, slot in enumerate(self.inventory.slots, 1):

                if slot.empty: 
                    print(f"  [{slot.item}]", end= " ")
                
                else:
                    print(f"  [{str(slot.item)} {slot.item.name.capitalize()} x{slot.amount}]", end= " ")
                
                uti.row_break(index, 4, 2)
            

            action = uti.del_space(input("\nAction: ")).lower()

            print(action)
            
            if action == 'q':
                return
            
            elif action in ("equip", "craft"):
                mode = action
                continue

            match mode:

                case "craft":
                    self.craft_item(action)

                case "equip":
                    self.equip_item(action)
                
 
            
        

    def interact(self, world: list):
        
        step: list = self.direction_calc(self.facing)

        try:
            interact_object: WorldObject = world[self.y + step[0]][self.x + step[1]]
        
        except IndexError:
            return

        if interact_object.collision == False:
            return

        match interact_object.category:

            case Category.HARVESTABLE:
                
                interact_object.harvest(self, world)
    
    
    def input_handler(self, world: list):
    
        if len(self.input_queue) == 0:
            
            incoming_input = list(input(" Action: ").strip())

            if len(incoming_input) == 0: return
            
            self.input_queue.extend(incoming_input)
            

        if self.input_queue[0] in controls["movement"]:
            
            self.facing = self.input_queue[0]
            
            self.movement(self.input_queue[0], world)
        
        elif self.input_queue[0] == controls["interact"]:
            
            self.interact(world)
        
        elif self.input_queue[0] == controls["inventory"]:
            
            self.open_inventory()
        
        else:
            pass

        self.input_queue.pop(0)
        

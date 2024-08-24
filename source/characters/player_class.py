
import utility as uti
import materials.harvestable_class as har
import materials.resources as res

from materials.item_dict import item_dict
from characters.character_class import Character
from misc_classes.object_class import GameObject
from misc_classes.storage_class import Storage

from enviorment.ground import Grass


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



class Player(GameObject, Character):
    
    def __init__(self, world: list) -> None:
        
        super().__init__(" i", 0, 10)
        Character.__init__(self)

        self.input_queue = []
        self.inventory = Storage(12, 10, "-Empty-", "Inventory")

        #For devolopement, so no need to harvest resources
        for _ in range(3):
            self.inventory.add_item(res.Wood())

        world[self.y][self.x] = self

    
    def display_hud(self):
        
        print(f" {uti.bold("Facing: ")}{facing_directions[self.facing]}", end="")
        
        print(f"{uti.bold("Health: "):>50}{self.health}")


    def count_items(self):

        item_count = {}
        
        for slot in self.inventory.slots:

            if slot.empty: continue

            elif slot.item.name in item_count:

                item_count[slot.item.name] += slot.amount

            else:
                item_count[slot.item.name] = slot.amount
        
        return item_count


    def craft_item(self, action: str):

        item = item_dict[action.capitalize()]
        
        inventory_count = self.count_items()
        
        
        for ingredient in item.recipe.keys():
            
            if ingredient in inventory_count and inventory_count[ingredient] >= item.recipe[ingredient]:
                continue

            else:
                return
        
        self.inventory.add_item(item)
            

    def open_inventory(self):

        while True:

            uti.clear()
            
            print(uti.bold(self.inventory.name + ": "), end="\n\n")

            for index, slot in enumerate(self.inventory.slots, 1):

                if slot.empty: 
                    print(f"  [{slot.item}]", end= " ")
                
                else:
                    print(f"  [{str(slot.item)} {slot.item.name} x{slot.amount}]", end= " ")
                
                uti.row_break(index, 4, 2)
            

            action = input("\nAction: ")
            
            try:
                self.craft_item(action)
            
            except ValueError: 
                break
        

    def interact(self, world: list):
        
        step = self.direction_calc(self.facing)

        try:
            interact_object = world[self.y + step[0]][self.x + step[1]]
        
        except IndexError:
            return

        if interact_object.collision == False:
            return

        if isinstance(interact_object, har.Harvestable):
            
            self.ground = Grass()
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
        

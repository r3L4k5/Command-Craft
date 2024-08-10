
import utility as uti

import Classes.resource_class as res

from Classes.character_class import Character
from Classes.object_class import GameObject

from Classes.storage_class import Storage
from enviorment import Grass



controls = {
    "movement": ['w', 's', 'a', 'd'],
    "inventory": 'q',
    "interact": 'e'
}

navigation = {
    'w': "North",
    's': "South",
    'a': "West",
    'd': "East"
}

crafting_space = Storage(9, 10, "Crafting Space")

for index, slot in enumerate(crafting_space.slots, 1): slot.item = "-" + str(index) + "-"


class Player(GameObject, Character):
    
    def __init__(self, world) -> None:
        
        super().__init__(" i", 0, 10)
        Character.__init__(self)

        self.input_queue = []
        self.inventory = Storage(12, 10, "-Empty-", "Inventory")

        world[self.y][self.x] = self

    
    def display_hud(self):
        
        print(f" {uti.bold("Facing: ")}{navigation[self.facing]}", end="")
        
        print(f"{uti.bold("Health: "):>50}{self.health}")


    def select_items(self, action: str, crafting_space: Storage):
         
        action = action.split("-")
        

        place =  int(action[0]) - 1     
        
        resource = res.resource_dict[action[1].capitalize()]


        total_amount = [slot.amount for slot in self.inventory.slots if type(slot.item) == type(resource)]
        
        resource_amount = uti.clamp(int(action[2]), max= total_amount, min= 0 )
    

        crafting_space.add_item_specific(res.resource_dict[resource](resource_amount), place)
    
        self.inventory.remove_item(res.resource_dict[resource](resource_amount), "-Empty-")
        
        self.open_inventory()


    def open_inventory(self):
        
        while True:

            uti.cls()
            
            print(uti.bold(self.inventory.name + ": "), end="\n\n")

            
            for index, slot in enumerate(crafting_space.slots, 1):

                if slot.empty: 
                    print(f"[{slot.item}]", end= " ")

                else:
                    print(f"[{str(slot.item)} x {slot.amount}]", end= " ")
                
                uti.row_break(index, 3, 1)
            
            print()

            for index, slot in enumerate(self.inventory.slots, 1):

                if slot.empty: 
                    print(f"  [{slot.item}]", end= " ")
                
                else:
                    print(f"  [{str(slot.item)} {slot.item.name} x{slot.amount}]", end= " ")
                
                uti.row_break(index, 4, 2)
            

            action = input("\nAction: ")
            
            try: 
                self.select_items(action, crafting_space)
            
            except ValueError: break
        


    def interact(self, world: list):
        
        step = self.direction_calc(self.facing)

        try:
            interact_object = world[self.y + step[0]][self.x + step[1]]
        
        except IndexError:
            return

        if interact_object.collision == False:
            return

        if isinstance(interact_object, res.Harvestable):
            
            self.ground = Grass()
            interact_object.harvest(self, world)
    
    
    def input_handler(self, world: list):
    
        if len(self.input_queue) == 0:
            
            incoming_input = list(input(" Action: ").strip())

            if len(incoming_input) == 0:return
            
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
        


            
        



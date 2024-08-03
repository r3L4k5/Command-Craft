
import utility as uti

from character_class import Character, Stats
from object_class import GameObject, ObjectCategory
from resource_class import Harvestable



controls = {
    "movement": ['w', 's', 'a', 'd'],
    "inventory": 'q',
    "interact": 'e',
    "change_facing": 'c'
}

navigation = {
    'w': "North",
    's': "South",
    'a': "West",
    'd': "East"
}


class Player(GameObject, Character):
    
    def __init__(self, world) -> None:
        
        super().__init__(" i", 0, 10, ObjectCategory.PLAYER)
        Character.__init__(self, stats= Stats())

        self.input_queue = []
        self.inventory = []

        world[self.y][self.x] = self

    
    def display_hud(self):
        
        print(f" {uti.bold("Facing: ")}{navigation[self.facing]} {uti.bold("Health: "):>50}{self.stats.health}")
    
    
    def open_inventory(self):
        uti.cls()
        
        print(uti.bold("Inventory: "), end="\n\n")

        for slot in self.inventory:
            print(f"    {slot["item"].sprite} {slot["item"].name} x {slot["amount"]}", end="\n\n")
            #print("    ----------------------")
        
        if input("'e' to exit: ") == 'e':
            return
        
        uti.cls()


    def interact(self, world):
        
        step = self.direction_calc(self.facing)

        interact_object = world[self.y + step[0]][self.x + step[1]]

        if interact_object.collision == False:
            return

        if isinstance(interact_object, Harvestable):
            
            interact_object.harvest(self, world)
    
    
    def input_handler(self, world):
        
        if len(self.input_queue) == 0:
            
            incoming_input = list(input(" Action: ").strip())
            
            self.input_queue.extend(incoming_input)
            

        if len(self.input_queue) != 0:
        
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
        


            
        



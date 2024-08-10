
import utility as uti

from Classes.character_class import Character, Stats
from Classes.object_class import GameObject
from Classes.resource_class import Harvestable
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


class Player(GameObject, Character):
    
    def __init__(self, world) -> None:
        
        super().__init__(" i", 0, 10)
        Character.__init__(self)

        self.input_queue = []
        self.inventory = []

        world[self.y][self.x] = self

    
    def display_hud(self):
        
        print(f" {uti.bold("Facing: ")}{navigation[self.facing]}", end="")
        
        print(f"{uti.bold("Health: "):>50}{self.health}")

        
       
    def open_inventory(self):
        uti.cls()
        
        print(uti.bold("Inventory: "), end="\n\n")


        while True:
            
            index = 1
            
            for slot in self.inventory:
                
                print(f"  {slot["item"].sprite} {slot["item"].name} x {slot["amount"]}", end=" ")

                if index % 4 == 0: print("\n")
                
                index += 1
            

            action = input("\n\nAction: ")
            
            if action == 'e': break
        
        
        uti.cls()


    def interact(self, world):
        
        step = self.direction_calc(self.facing)

        try:
            interact_object = world[self.y + step[0]][self.x + step[1]]
        
        except IndexError:
            return

        if interact_object.collision == False:
            return

        if isinstance(interact_object, Harvestable):
            self.ground = Grass()
            interact_object.harvest(self, world)
    
    
    def input_handler(self, world):
        
        if len(self.input_queue) == 0:
            
            incoming_input = list(input(" Action: ").strip())

            if len(incoming_input) == 0:
                return
            
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
        


            
        



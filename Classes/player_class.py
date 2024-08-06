
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


    def craft(self, action, crafting_space):
        
        specifications = action.split("-")

        print(specifications)
        matching_resource = list(filter(lambda slot: slot["item"].name == specifications[1], self.inventory))
        print(matching_resource)

        if len(matching_resource) == 0:
            print("none")

        for resource in matching_resource:

            if resource["amount"] > int(specifications[2]):
                resource["amount"] - int(specifications[2])
                print("W")
                break
            
            else:
                int(specifications[2]) - resource["amount"]
                self.inventory.remove[matching_resource]
                print("Del")

        

        #print(crafting_space[int(specifications[0])- 1])

        input()
        
       
    def open_inventory(self):
        uti.cls()
        
        print(uti.bold("Inventory: "), end="\n\n")

        crafting_space = [[ 1 ],[ 2 ],[ 3 ],[ 4 ]]

        while True:
            
            print(f"\n{crafting_space[0]}{crafting_space[1]}{"\n"}{crafting_space[2]}{crafting_space[3]}", end="\n\n")

            index = 1
            
            for slot in self.inventory:
                
                print(f"  {slot["item"].sprite} {slot["item"].name} x {slot["amount"]}", end=" ")

                if index % 4 == 0: print("\n")
                
                index += 1
            

            action = input("\n\nAction: ")
            
            if action == 'e': break
            
            self.craft(action, crafting_space)
        
        
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
        


            
        




import utility as uti
import Classes.resource_class as res

from Classes.character_class import Character
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

crafting_space = [[' 1 ',""], [' 2 ', ""], [' 3 ',""], [' 4 ',""]]


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


    def select_items(self, action, crafting_space):
         
        action = action.split("-")
        
        details = {"Place": int(action[0]) - 1, 
                
                "Resource": action[1].capitalize(), 

                "Amount": int(action[2])}
    

        matching_resource = list(filter(lambda item: item.name == details["Resource"], self.inventory))

        if len(matching_resource) == 0: self.open_inventory()

        if crafting_space[details["Place"]][0] == res.resource_dict[details["Resource"]].sprite:
            
            crafting_space[details["Place"]][1] += details["Amount"]
        
        else:

            crafting_space[details["Place"]][0] = res.resource_dict[details["Resource"]].sprite
            crafting_space[details["Place"]][1] = details["Amount"]


        for resource in matching_resource:

            if resource.amount > details["Amount"]:
                resource.amount -= details["Amount"]
            
            else:
                details["Amount"] -= resource.amount
                self.inventory.remove(resource)

        self.open_inventory()


    def open_inventory(self):
        
        uti.cls()
        
        print(uti.bold("Inventory: "), end="\n\n")

        while True:

            for index, item in enumerate(crafting_space, 1):
                
                print("[", item[0], item[1], "]" , end="")
                
                if index == 2: 
                    print()
            
            print("\n")

            for index, item in enumerate(self.inventory, 1):
                
                print(f"  {item.sprite} {item.name} x {item.amount}", end=" ")
                
                if index % 4 == 0: 
                    print("\n")
    
            
            action = input("\n\nAction: ")
            
            if action == 'e': 
                break
            
            self.select_items(action, crafting_space)
        
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
        


            
        



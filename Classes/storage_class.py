


class Slot():
    
    def __init__(self, item: str = "Empty", amount: int = 0, ) -> None:
        
        self.item = item
        self.amount = amount
        self.empty = True
        
    
    def empty_slot(self, placeholder = "Empty"):
        
        self.item = placeholder
        self.amount = 0
        self.empty = True        

class Storage():
    
    def __init__(self, size: int, max_stack: int, placeholder: str = "Empty", name: str = "Storage") -> None:
        
        self.slots = [Slot(placeholder) for _ in range(size)]
        self.max_stack = max_stack
        self.name = name
    
    def add_item_specific(self, item, place):
        
        target = self.slots[place]
        new_amount = target.amount + item.amount
  
        if new_amount >= self.max_stack :
            
            target.amount = self.max_stack
            item.amount -= self.max_stack

            return item

        elif type(target.item) == type(item):
                    
            target.amount += new_amount
        
        elif target.empty:

            target.item = item
            target.amount = item.amount
        
        target.empty = False


    def add_item(self, new_item):
        
        matching_slots = list(filter(lambda slot: type(slot.item) == type(new_item), self.slots))

        for slot in matching_slots:
            
            new_amount = slot.amount + new_item.amount
            
            if new_amount < self.max_stack:
                
                slot.amount += new_item.amount
                return
            
            elif new_amount >= self.max_stack:
                
                new_item.amount = new_amount - self.max_stack
                slot.amount = self.max_stack

        
        empty_slots = list(filter(lambda slot: slot.empty, self.slots))            
        
        for slot in empty_slots:
        
            if new_item.amount <= self.max_stack:
                
                slot.item = new_item
                slot.amount += new_item.amount
                
                slot.empty = False
                
                return 
            
            elif new_item.amount > self.max_stack:

                slot.item = new_item
                slot.amount = self.max_stack
                new_item.amount -= self.max_stack

                slot.empty = False 
            
        return new_item
    

    def remove_item(self, del_item, placeholder = None):

        matching_slots = list(filter(lambda slot: type(slot.item) == type(del_item), self.slots))

        for slot in matching_slots:

            new_amount = slot.amount - del_item.amount
            
            if new_amount > 0:
                slot.amount = new_amount
                break
            
            else:
                del_item.amount -= slot.amount
                slot.empty_slot(placeholder)

        return del_item
            

if __name__ == "__main__":
    
    import resource_class as res
    
    store = Storage(7, 2)

    store.add_item(res.Wood(3))

    print(list(str(slot.item) for slot in store.slots))
    print(list(slot.amount for slot in store.slots))

    store.remove_item(res.Wood(3), "Empty")

    print(list(str(slot.item) for slot in store.slots))
    print(list(slot.amount for slot in store.slots))




            


        










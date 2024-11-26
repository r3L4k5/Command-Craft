
from items.items import Item

class Slot():
    
    def __init__(self, item: str | Item = "-Empty-", amount: int = 0) -> None:
        
        self.item = item
        
        if hasattr(self.item, "amount"):
            self.item.amount = amount

        self.empty = True
        
    def empty_slot(self, placeholder: str = "-Empty-"):

        self.item = placeholder
        self.empty = True

    def __str__(self) -> str:

        return f"[{self.item}]"


class Storage():
    
    def __init__(self, size: int, max_stack: int, placeholder: str = "-Empty-", name: str = "Storage") -> None:
        
        self.slots = [Slot(placeholder) for _ in range(size)]
        self.max_stack = max_stack
        self.name = name
    

    def add_item(self, new_item: Item):
    
        matching_slots = list(filter(lambda slot: slot.item == new_item, self.slots))

        for slot in matching_slots:

            new_amount = slot.item.amount + new_item.amount
            
            if new_amount <= self.max_stack:
                slot.item.amount = new_amount
                return
            
            elif new_amount > self.max_stack:
                
                new_item.amount = new_amount - self.max_stack
                slot.item.amount = self.max_stack

        
        empty_slots = list(filter(lambda slot: slot.empty, self.slots))            
        
        for slot in empty_slots:

            slot.empty = False 
        
            if new_item.amount <= self.max_stack:
                
                slot.item = new_item
                return 
            
            elif new_item.amount > self.max_stack:

                slot.item = new_item
                slot.item.amount = self.max_stack
                
                new_item.amount -= self.max_stack

        return new_item
    

    def remove_item(self, del_item: Item):

        matching_slots = list(filter(lambda slot: slot.item == del_item, self.slots))

        for slot in matching_slots:

            new_amount = slot.item.amount - del_item.amount
            
            if new_amount > 0:
                slot.item.amount = new_amount
                return
            
            else:
                del_item.amount -= slot.item.amount
                slot.empty_slot()
            
        else:
            return del_item
    
    def count_items(self) -> dict:

        item_count = {}
        
        for slot in self.slots:

            if slot.empty: 
                continue

            elif slot.item.name in item_count:

                item_count[slot.item.name] += slot.item.amount

            else:
                item_count[slot.item.name] = slot.item.amount
        
        return item_count



    



            


        










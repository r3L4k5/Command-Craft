
from systems.storage import Storage

import importlib as imp


class Craftable():

    def __init__(self, recipe: dict[str:int]):

        self.recipe = recipe


    def craft(self, source: Storage) -> bool:
        
        storage_count: dict[str:int] = source.count_items()

        consumed_list: list = []

        for ingredient in self.recipe.keys():

            if ingredient in storage_count and storage_count[ingredient] >= self.recipe[ingredient]:
                
                consumed = imp.import_module("items.item_access").get_item(ingredient)
                consumed.amount = self.recipe[ingredient]

                consumed_list.append(consumed)

            else:
                return False
            
        for consumed in consumed_list:

           source.remove_item(consumed)
        
        return True
        
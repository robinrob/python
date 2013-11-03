from generator import Generator
from my_exceptions import EmptyBagException

class GrabBag:
    
    def __init__(self, items):
        self.items = items
        
        
    def grab_item(self):
        if (len(self.items) > 0):
            index = Generator().rand_num(len(self.items))
            item = self.items[index]
            self.items.remove(item)
            return item
        else:
            raise EmptyBagException
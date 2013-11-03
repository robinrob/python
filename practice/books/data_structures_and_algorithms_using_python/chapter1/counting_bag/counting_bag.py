from generator import Generator
from my_exceptions import EmptyBagException

class CountingBag:

    def __init__(self, items):

        self.items = {}

        for item in items:
            if not item in self.items.keys():
                self.items[item] = 1

            else:
                self.items[item] += 1


    def grab_item(self):

        if (len(self.items.keys()) > 0):
            index = Generator().rand_num(len(self.items.keys()))
            item = list(self.items.keys())[index]
            self.remove_one(self.items, item)


            return item

        else:
            raise EmptyBagException


    @staticmethod
    def remove_one(items, item):

        if item in items:
            if items[item] == 1:
                items.pop(item, None)

            else:
                items[item] -= 1

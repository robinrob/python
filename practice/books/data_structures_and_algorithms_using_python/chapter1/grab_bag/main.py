from grab_bag import GrabBag
from my_exceptions import EmptyBagException

items = []

for i in range(0, 30):
    items.append(chr(ord('A') + i))
    
bag = GrabBag(items)

while True:
    try:
        print(str(bag.grab_item()))
    except EmptyBagException:
        print("Bag Empty")
        break
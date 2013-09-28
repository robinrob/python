from counting_bag import CountingBag
from my_exceptions import EmptyBagException

items = []

for i in range(0, 26):
    items.append(chr(ord('A') + i))
    items.append(chr(ord('A') + i))
    
bag = CountingBag(items)

while True:
    try:
        print(str(bag.grab_item()))

    except EmptyBagException:
        print("Bag Empty")
        break
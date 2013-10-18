class RobinSet:

    def __init__(self):
        self._items = []


    def add(self, item):
        if item not in self:
            self._items.append(item)


    def remove(self, item):
        try:
            self._items.remove(item)

        except RuntimeError:
            print("Fuck off!")


    def is_subset_of(self, other):
        if len(other) > len(self) and len(self) > 0:
            for item in self:
                if item not in other:
                    return False

            return True


    def union(self, other):
        union = RobinSet()
        for item in self:
            union.add(item)

        for item in other:
            if item not in self:
                union.add(item)

        return union


    def intersect(self, other):
        intersect = RobinSet()
        for item in self:
            if item in other:
                intersect.add(item)

        return intersect



    def difference(self, other):
        difference = RobinSet()
        for item in self:
            if item not in other:
                difference.add(item)

        for item in other:
            if item not in self:
                difference.add(item)

        return difference


    def __len__(self):
        return len(self._items)


    def __contains__(self, item):
        return item in self._items


    def __eq__(self, other):
        if len(other) is len(self):
            for item in self:
                if item not in other:
                    return False

            return True


    def __iter__(self):
        return iter(self._items)


    def __str__(self):
        s = ""

        for item in self:
            s += str(item) + " "

        return s
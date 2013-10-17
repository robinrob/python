class RobinSet:

    def __init__(self):
        self.set = []


    def __len__(self):
        return len(self.set)


    def __contains__(self, item):
        return item in self.set


    def add(self, item):
        if item not in self:
            self.set.append(item)


    def remove(self, item):
        try:
            self.set.remove(item)

        except RuntimeError:
            print("Fuck off!")


    def __eq__(self, other):
        if len(other) is len(self):
            for item in self:
                if item not in other:
                    return False

            return True


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



    def __iter__(self):
        return iter(self.set)


    def __str__(self):
        s = ""

        for item in self:
            s += str(item) + " "

        return s
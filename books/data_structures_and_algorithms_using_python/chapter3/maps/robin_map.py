class RobinMap:

    def __init__(self):
        self._keys = []
        self._values = []
        self._next = None


    def __len__(self):
        return len(self._keys)


    def __contains__(self, item):
        if item in self._keys:
            return True


    def __iter__(self):
        self._next = 0
        return iter(self._keys)


    def put(self, key, value):
        if key not in self:
            self._keys.append(key)
            self._values.append(value)
        else:
            self._values[self._keys.index(key)] = value


    def remove(self, key):
        if key in self:
            self._values.remove(self.get(key))
            self._keys.remove(key)


    def get(self, key):
        if key in self:
            return self._values[self._keys.index(key)]
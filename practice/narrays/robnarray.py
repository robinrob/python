import copy

from robarray import RobArray

class RobNArray:

    def __init__(self, *args):
        self.args = args
        self.dims = len(args)
        self._elements = self._init_elements(args, None)


    def _init_elements(self, args, value):
        self.dims = 0
        elements = value

        for i in reversed(range(len(args))):
            self.dims += 1
            elements = self._add_dimension(elements, args[i])

        return elements


    def _add_dimension(self, elements, size):
        return RobArray(size, copy.copy(elements))


    def add_inner_dimension(self, size, value):
        self.args = (size,) + self.args
        self._elements = self._add_dimension(self._elements, size)


    def add_outer_dimension(self, size, value):
        self.args = self.args + (size,)
        self._elements = self._init_elements(self.args, value)


    def get_item(self, *coords):
        value = self._elements

        for coord in coords:
            print("value: " + str(value))
            value = value[coord]

        return value


    def set_item(self, value, *coords):
        element = self._elements

        list_coords = list(coords)
        for coord in list_coords:
            if coord is list_coords[-1]:
                element[coord] = value

            else:
                element = element[coord]


    def dims(self):
        return self.dims


    def clear(self, value):
        self._elements = self._init_elements(self.args, value)


    def __len__(self):
        element = self._elements
        length = len(element)

        while isinstance(element[0], RobArray):
            length *= len(element[0])
            element = element[0]

        return length
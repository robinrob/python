import copy

from robarray import RobArray

class LinearNArray:

    def __init__(self, *args):
        self._args = args

        self._dims = len(args)

        self._length = self._calc_length(args)

        self._elements = RobArray(self._length)


    def _calc_length(self, *dims):
        length = 0
        for dim in dims:
            length *= dim

        return length


    def get_item(self, *coords):
        pass


    def set_item(self, value, *coords):
        pass


    def dims(self):
        return self._dims


    def clear(self, value):
        pass


    def __len__(self):
        return self._length
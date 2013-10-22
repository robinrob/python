#import unittest
#
#from linearnarray import LinearNArray
#
#class TestRobNArray(unittest.TestCase):
#
#    def test_should_initialise_1_by_1_array(self):
#        arr = LinearNArray(1)
#
#        self.assertEquals(1, len(arr))
#
#
#    def test_should_initialise_2_by_2_array(self):
#        arr = LinearNArray(2, 2)
#
#        self.assertEquals(4, len(arr))
#        self.assertEquals(2, len(arr.get_item(0)))
#
#
#    def test_should_get_and_set_items(self):
#        coords = (1, 1)
#        value = 99
#        arr = LinearNArray(2, 2)
#
#        arr.set_item(value, coords)
#
#        self.assertEquals(value, len(arr.get_item(coords)))
#
#
#    def test_should_initialise_10_by_10_array(self):
#        arr = LinearNArray(10, 10, 10, 10, 10, 10, 10, 10, 10, 10)
#
#        self.assertEquals(10, len(arr.get_item(0, 0, 0, 0, 0, 0, 0, 0, 0)))
#
#
#    def test_should_clear_1_by_1_array_with_0(self):
#        arr = LinearNArray(1)
#
#        arr.clear(0)
#
#        self.assertEquals(0, arr.get_item(0))
#
#
#    def test_should_clear_10_by_10_array_with_0(self):
#        arr = LinearNArray(10, 10, 10, 10, 10, 10, 10, 10, 10, 10)
#
#        arr.clear(0)
#
#        self.assertEquals(0, arr.get_item(0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
#
#
#    def test_should_return_number_of_dimension(self):
#        expected = 10
#        dims = (1)
#        for i in range(expected - 1):
#            dims += (1,)
#        arr = LinearNArray(dims)
#
#        actual = arr.dims()
#
#        self.assertEquals(expected, actual)
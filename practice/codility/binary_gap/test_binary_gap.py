import unittest

from binary_gap import binary_gap

class BinaryGapTestCase(unittest.TestCase):

    def test_shouldwork(self):
        self.assertEquals(0, binary_gap(0))
        self.assertEquals(0, binary_gap(1))
        self.assertEquals(0, binary_gap(3))
        self.assertEquals(0, binary_gap(4))
        self.assertEquals(1, binary_gap(5))
        self.assertEquals(2, binary_gap(9))
        self.assertEquals(1, binary_gap(11))
        self.assertEquals(4, binary_gap(33))
        self.assertEquals(6, binary_gap(129))
        self.assertEquals(5, binary_gap(1049))
        self.assertEquals(29, binary_gap(1073741825))
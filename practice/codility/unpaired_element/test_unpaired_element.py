import unittest

from unpaired_element import unpaired_element

class UnpairedElementTestCase(unittest.TestCase):
    def test_should_find_unpaired_element(self):
        self.assertEquals(
            1,
            unpaired_element([1])
        )

        self.assertEquals(
            1,
            unpaired_element([1, 2, 2])
        )

        self.assertEquals(
            1,
            unpaired_element([3, 4, 5, 5, 4, 3, 1, 3, 4, 5, 5, 4, 3, 1, 3, 4, 5, 5, 4, 3, 1, 3, 4, 5, 5, 4, 3, 1, 3, 4, 5, 5, 4, 3, 1, 3, 4, 5, 5, 4, 3, 1, 3, 4, 5, 5, 4, 3, 1])
        )
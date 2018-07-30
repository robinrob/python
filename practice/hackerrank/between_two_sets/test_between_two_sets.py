import unittest

from between_two_sets import get_num_between

class BetweenTwoSetsTestCase(unittest.TestCase):
    def test_should_be_0_between_1(self):
        num_between = get_num_between(
            [1, 2, 3],
            [1, 2, 3]
        )

        self.assertEquals(0, num_between)

    def test_should_be_1_between_1(self):
        num_between = get_num_between(
            [1, 2, 3],
            [6, 12, 24]
        )

        self.assertEquals(1, num_between)


    def test_should_be_2_between_1(self):
        num_between = get_num_between(
            [1, 2, 3],
            [12, 24]
        )

        self.assertEquals(2, num_between)


    def test_should_be_3_between_1(self):
        num_between = get_num_between(
            [3],
            [24, 36]
        )

        self.assertEquals(3, num_between)
import unittest

from apple_and_orange import count_apples_and_oranges

class AppleAndOrangeTestCase(unittest.TestCase):

    def test_should_be_0_apples_and_0_oranges(self):
        num_apples, num_oranges = count_apples_and_oranges(
            5, 10, 0, 15,
            [0],
            [15]
        )

        self.assertEquals(0, num_apples)
        self.assertEquals(0, num_oranges)


    def test_should_be_1_apples_and_1_oranges(self):
        num_apples, num_oranges = count_apples_and_oranges(
            5, 10, 0, 15,
            [7],
            [-7]
        )

        self.assertEquals(1, num_apples)
        self.assertEquals(1, num_oranges)

    def test_should_be_2_apples_and_2_oranges(self):
        num_apples, num_oranges = count_apples_and_oranges(
            5, 10, 0, 15,
            [5, 10],
            [-5, -10]
        )

        self.assertEquals(2, num_apples)
        self.assertEquals(2, num_oranges)
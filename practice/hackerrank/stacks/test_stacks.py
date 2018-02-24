import unittest

from stacks import _play


class StacksTestCase(unittest.TestCase):

    def test_should_return_0(self):
        x = 0
        a = []
        b = []

        score = _play(x, a, b)

        self.assertEquals(0, score)


    def test_should_return_1(self):
        x = 1
        a = [1]
        b = []

        score = _play(x, a, b)

        self.assertEquals(1, score)


    def test_should_return_0_with_x_0(self):
        x = 0
        a = [1]
        b = []

        score = _play(x, a, b)

        self.assertEquals(0, score)


    def test_should_return_4_from_stack_a(self):
        x = 10
        a = [1, 2, 3, 4]
        b = []

        score = _play(x, a, b)

        self.assertEquals(4, score)


    def test_should_return_4_from_stack_b(self):
        x = 10
        a = []
        b = [1, 2, 3, 4]

        score = _play(x, a, b)

        self.assertEquals(4, score)


    def test_should_return_4_from_stack_a_and_b(self):
        x = 10
        a = [1, 2]
        b = [3, 4]

        score = _play(x, a, b)

        self.assertEquals(4, score)


    def test_should_return_5_from_stack_a_and_b(self):
        x = 10
        a = [5, 1, 1, 1, 1]
        b = [2, 3, 3, 3, 3]

        score = _play(x, a, b)

        self.assertEquals(5, score)


    def test_should_return_4_for_example(self):
        x = 10

        a = [4, 2, 4, 6, 1]
        b = [2, 1, 8, 5]

        score = _play(x, a, b)

        self.assertEquals(4, score)

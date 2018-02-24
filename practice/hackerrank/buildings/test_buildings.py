import unittest

from buildings import _calc


class StacksTestCase(unittest.TestCase):

    def test_should_return_0(self):
        area = _calc([0, 0, 0, 0, 0])

        self.assertEquals(0, area)


    def test_should_return_4(self):
        area = _calc([1, 1, 1, 1])

        self.assertEquals(4, area)


    def test_should_return_2(self):
        area = _calc([0, 1, 1, 0])

        self.assertEquals(2, area)


    def test_should_return_16(self):
        area = _calc([2, 8, 8, 2])

        self.assertEquals(16, area)


    def test_should_return_1(self):
        area = _calc([1, 0, 1, 0])

        self.assertEquals(1, area)


    def test_should_return_12(self):
        area = _calc([2, 3, 2, 3, 2, 2])

        self.assertEquals(12, area)


    def test_should_return_50(self):
        area = _calc([2, 0, 25, 25, 2, 10, 0])

        self.assertEquals(50, area)


    def test_should_return_50_again(self):
        area = _calc([0, 0, 0, 25, 25])

        self.assertEquals(50, area)


    def test_should_return_12_again(self):
        area = _calc([1, 2, 3, 4, 5, 6])

        self.assertEquals(12, area)


    def test_should_return_8(self):
        area = _calc([4, 3, 2, 3, 2, 3, 4, 3])

        self.assertEquals(16, area)


    def test_should_return_9_for_example(self):
        area = _calc([1, 2, 3, 4, 5])

        self.assertEquals(9, area)
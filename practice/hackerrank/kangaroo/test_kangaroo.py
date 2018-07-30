import unittest

from kangaroo import kangaroo

class KangarooTestCase(unittest.TestCase):

    def test_should_be_yes_0_10_5_5(self):
        yes_or_no = kangaroo(0, 10, 5, 5)

        self.assertEquals('YES', yes_or_no)

    def test_should_be_yes_0_8_4_4(self):
        yes_or_no = kangaroo(0, 8, 4, 4)

        self.assertEquals('YES', yes_or_no)

    def test_should_be_yes_0_10_5_5(self):
        yes_or_no = kangaroo(0, 10, 5, 5)

        self.assertEquals('YES', yes_or_no)

    def test_should_be_no_0_2_5_3(self):
        yes_or_no = kangaroo(0, 2, 5, 3)

        self.assertEquals('NO', yes_or_no)
import unittest

from robinset import RobinSet

class TestRobinSet(unittest.TestCase):

    def test_should_add_item(self):
        set = RobinSet()
        value = 0

        set.add(value)

        self.assertTrue(value in set)


    def test_should_remove_item(self):
        set = RobinSet()
        value = 0
        set.add(value)

        set.remove(value)

        self.assertTrue(value not in set)


    def test_should_be_equal_to_other_set_when_both_empty(self):
        set = RobinSet()

        otherset = RobinSet()

        self.assertEquals(set, otherset)


    def test_should_be_equal_to_other_set_when_both_have_1_item(self):
        value = 0

        set = RobinSet()
        set.add(value)
        otherset = RobinSet()
        otherset.add(value)

        self.assertEquals(set, otherset)
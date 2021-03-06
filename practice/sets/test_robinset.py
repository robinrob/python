import unittest

from robinset import RobinSet

class TestRobinSet(unittest.TestCase):

    def test_new_set_should_be_empty(self):
        set = RobinSet()

        self.assertEquals(0, len(set))


    def test_should_add_item_when_empty(self):
        set = RobinSet()
        value = 0

        set.add(value)

        self.assertTrue(value in set)


    def test_should_not_add_item_if_already_there(self):
        set = RobinSet()
        value = 0
        set.add(value)

        set.add(value)

        self.assertTrue(1, len(set))


    def test_should_throw_value_error_when_removing_item_from_empty_set(self):
        set = RobinSet()

        self.assertRaises(ValueError, set.remove, 0)


    def test_should_remove_item(self):
        set = RobinSet()
        value = 0
        set.add(value)

        set.remove(value)

        self.assertTrue(value not in set)


    def test_should_be_equal_to_other_set_when_both_empty(self):
        set = RobinSet()

        other_set = RobinSet()

        self.assertEquals(set, other_set)


    def test_should_be_equal_to_other_set_when_both_have_1_item(self):
        self.should_be_equal_to_other_set_when_both_have_n_items(1)


    def test_should_be_equal_to_other_set_when_both_have_10_items(self):
        self.should_be_equal_to_other_set_when_both_have_n_items(10)


    def should_be_equal_to_other_set_when_both_have_n_items(self, n_items):
        set = RobinSet()
        other_set = RobinSet()

        for i in range(0, n_items):
            set.add(i)
            other_set.add(i)

        self.assertEquals(set, other_set)


    def test_should_not_be_subset_of_other_set_when_both_empty(self):
        set = RobinSet()
        other_set = RobinSet()

        self.assertFalse(set.is_subset_of(other_set))


    def test_should_not_be_subset_of_other_set_when_set_is_empty(self):
        set = RobinSet()
        other_set = RobinSet()
        other_set.add(0)

        self.assertFalse(set.is_subset_of(other_set))


    def test_should_not_be_subset_of_other_set_when_other_set_is_empty(self):
        set = RobinSet()
        set.add(0)
        other_set = RobinSet()

        self.assertFalse(set.is_subset_of(other_set))


    def test_should_not_be_subset_of_other_set_when_other_set_is_smaller(self):
        set = RobinSet()
        set.add(0)
        set.add(1)
        other_set = RobinSet()
        other_set.add(0)

        self.assertFalse(set.is_subset_of(other_set))


    def test_should_not_be_subset_of_other_set(self):
        set = RobinSet()
        set.add(0)
        other_set = RobinSet()
        other_set.add(0)
        other_set.add(1)

        self.assertTrue(set.is_subset_of(other_set))


    def test_should_return_empty_set_for_union_of_two_empty_sets(self):
        set = RobinSet()
        other_set = RobinSet()

        union = set.union(other_set)

        self.assertEquals(0, len(union))


    def test_should_return_set_for_union_with_empty_set(self):
        set = RobinSet()
        set.add(0)
        other_set = RobinSet()

        union = set.union(other_set)

        self.assertEquals(set, union)


    def test_should_return_other_set_for_union_with_non_empty_set(self):
        set = RobinSet()
        other_set = RobinSet()
        other_set.add(0)

        union = set.union(other_set)

        self.assertEquals(other_set, union)


    def test_should_return_set_for_union_with_identical_set(self):
        set = RobinSet()
        set.add(0)
        other_set = RobinSet()
        other_set.add(0)

        union = set.union(other_set)

        self.assertEquals(set, union)


    def test_should_return_union_with_2_items(self):
        set = RobinSet()
        set.add(0)
        other_set = RobinSet()
        other_set.add(1)

        union = set.union(other_set)

        self.assertEquals(2, len(union))


    def test_should_return_union_with_items_from_both_sets(self):
        set = RobinSet()
        set.add(0)
        other_set = RobinSet()
        other_set.add(1)

        union = set.union(other_set)

        self.assertTrue(0 in union)
        self.assertTrue(1 in union)


    def test_should_return_empty_set_for_intersect_of_empty_sets(self):
        set = RobinSet()
        other_set = RobinSet()

        intersect = set.intersect(other_set)

        self.assertEquals(RobinSet(), intersect)


    def test_should_return_empty_set_for_intersect_with_empty_set(self):
        set = RobinSet()
        set.add(0)
        other_set = RobinSet()

        intersect = set.intersect(other_set)

        self.assertEquals(RobinSet(), intersect)


    def test_should_return_empty_set_for_intersect_on_empty_set(self):
        set = RobinSet()
        other_set = RobinSet()
        other_set.add(0)

        intersect = set.intersect(other_set)

        self.assertEquals(RobinSet(), intersect)


    def test_should_return_set_for_intersect_on_equal_sets(self):
        set = RobinSet()
        set.add(0)
        other_set = RobinSet()
        other_set.add(0)

        intersect = set.intersect(other_set)

        self.assertEquals(set, intersect)


    def test_should_return_set_for_intersect_on_equal_sets(self):
        set = RobinSet()
        set.add(0)
        other_set = RobinSet()
        other_set.add(0)

        intersect = set.intersect(other_set)

        self.assertEquals(set, intersect)


    def test_should_common_items_for_intersect_on_sets(self):
        set = RobinSet()
        for i in range(0, 10):
            set.add(i)

        other_set = RobinSet()
        for i in range(5, 15):
            other_set.add(i)

        expected = RobinSet()
        for i in range(5, 10):
            expected.add(i)

        intersect = set.intersect(other_set)

        self.assertEquals(expected, intersect)


    def test_should_return_empty_set_for_difference_of_two_empty_sets(self):
        set = RobinSet()
        other_set = RobinSet()

        difference = set.difference(other_set)

        self.assertEquals(RobinSet(), difference)


    def test_should_return_set_for_difference_with_empty_set(self):
        set = RobinSet()
        set.add(0)
        other_set = RobinSet()

        difference = set.difference(other_set)

        self.assertEquals(set, difference)


    def test_should_return_other_set_for_difference_on_empty_set(self):
        set = RobinSet()
        other_set = RobinSet()
        other_set.add(0)

        difference = set.difference(other_set)

        self.assertEquals(other_set, difference)


    def test_should_return_empty_set_for_difference_between_equal_sets(self):
        set = RobinSet()
        set.add(0)
        other_set = RobinSet()
        other_set.add(0)

        difference = set.difference(other_set)

        self.assertEquals(RobinSet(), difference)


    def test_should_return_items_unique_to_both_sets(self):
        set = RobinSet()
        for i in range(0, 10):
            set.add(i)

        other_set = RobinSet()
        for i in range(5, 15):
            other_set.add(i)

        expected = RobinSet()
        for i in range(0, 5):
            expected.add(i)
        for i in range(10, 15):
            expected.add(i)

        difference = set.difference(other_set)

        self.assertEquals(expected, difference)
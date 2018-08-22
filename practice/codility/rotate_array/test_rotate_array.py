import unittest

from rotate_array import rotate_array

class RotateArrayTestCase(unittest.TestCase):

    def test_should_rotate_arrays(self):
        self.assertEqual(
            [3,1,2],
            rotate_array([1,2,3], 1)
        )

        self.assertEqual(
            [3,4,5,1,2],
            rotate_array([1,2,3,4,5], 3)
        )

        self.assertEqual(
            [],
            rotate_array([], 0)
        )

        self.assertEqual(
            [0],
            rotate_array([0], 10)
        )
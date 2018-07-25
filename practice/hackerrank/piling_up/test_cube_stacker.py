import unittest

from cube_stacker import can_stack_cubes


class CubeStackerTestCase(unittest.TestCase):

    def test_should_print_yes_for_no_cubes(self):
        cubes = []

        self.assertTrue(can_stack_cubes(cubes))

    def test_should_print_yes_for_1_cube(self):
        cubes = [1]

        self.assertTrue(can_stack_cubes(cubes))

    def test_should_print_yes_for_2_cubes(self):
        cubes = [1, 2]

        self.assertTrue(can_stack_cubes(cubes))

    def test_should_print_yes_for_3_cubes_when_possible(self):
        cubes = [1, 2, 3]

        self.assertTrue(can_stack_cubes(cubes))

    def test_should_print_no_for_3_cubes_when_not_possible(self):
        cubes = [1, 3, 2]

        self.assertFalse(can_stack_cubes(cubes))

    def test_should_print_yes_for_10_cubes_when_possible(self):
        cubes = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9]

        self.assertTrue(can_stack_cubes(cubes))

    def test_should_print_no_for_10_cubes_when_not_possible(self):
        cubes = [10, 8, 6, 4, 2, 3, 1, 5, 7, 9]

        self.assertFalse(can_stack_cubes(cubes))
import unittest

from matrix import Matrix

class TestMatrix(unittest.TestCase):

    def test_should_get_0_rows(self):
        self.should_get_num_rows(1)


    def test_should_get_100_rows(self):
        self.should_get_num_rows(100)


    def should_get_num_rows(self, num_rows):
        matrix = Matrix(1, num_rows)

        self.assertEqual(num_rows, matrix.num_rows())


    def test_should_get_0_cols(self):
        self.should_get_num_cols(0)


    def test_should_get_100_cols(self):
        self.should_get_num_cols(0)


    def should_get_num_cols(self, num_cols):
        matrix = Matrix(num_cols, 1)

        self.assertEqual(num_cols, matrix.num_cols())


    def test_should_set_and_get_first_row_of_first_column(self):
        matrix = Matrix(1, 1)
        val = 1
        matrix.set_item(0, 0, val)

        self.assertEquals(val, matrix.get_item(0, 0))


    def test_should_set_and_get_second_row_of_second_column(self):
        matrix = Matrix(2, 2)
        val = 1
        matrix.set_item(1, 1, val)

        self.assertEquals(val, matrix.get_item(1, 1))


    def test_should_iterate_over_1x1_matrix(self):
        self.should_iterate_over_matrix(1, 1)


    def test_should_iterate_over_2x2_matrix(self):
        self.should_iterate_over_matrix(2, 2)


    def test_should_iterate_over_1x10_matrix(self):
        self.should_iterate_over_matrix(1, 10)


    def test_should_iterate_over_10x1_matrix(self):
        self.should_iterate_over_matrix(10, 1)


    def test_should_iterate_over_2x2_matrix(self):
        self.should_iterate_over_matrix(2, 2)


    def should_iterate_over_matrix(self, cols, rows):
        matrix = Matrix(cols, rows)

        count = 0
        for element in matrix:
            count += 1

        self.assertEquals(cols * rows, count)
    

    def test_should_scale_by_0(self):
        self.should_scale_by_factor(0)


    def test_should_scale_by_1(self):
        self.should_scale_by_factor(1)


    def test_should_scale_by_pi(self):
        self.should_scale_by_factor(3.14)


    def should_scale_by_factor(self, factor):
        matrix = Matrix(1, 1, 1)

        matrix.scale_by(factor)

        self.assertEquals(factor, matrix.get_item(0, 0))


    def test_should_transpose_1x1_matrix(self):
        matrix = Matrix(1, 1, 1)

        matrix.transpose()

        self.assertEquals(1, matrix.get_item(0, 0))


    def test_should_have_1_row_after_tranpose(self):
        matrix = Matrix(1, 2, 1)

        matrix.transpose()

        self.assertEquals(1, matrix.num_rows())


    def test_should_have_1_column_after_tranpose(self):
        matrix = Matrix(2, 1, 1)

        matrix.transpose()

        self.assertEquals(1, matrix.num_cols())


    def test_should_have_10_rows_after_tranpose(self):
        matrix = Matrix(10, 100, 1)

        matrix.transpose()

        self.assertEquals(10, matrix.num_rows())


    def test_should_have_100_columns_after_tranpose(self):
        matrix = Matrix(2, 100, 1)

        matrix.transpose()

        self.assertEquals(100, matrix.num_cols())


    def test_should_contain_1337_in_last_column_after_transpose(self):
        cols = 1
        rows = 100
        matrix = Matrix(cols, rows, 1)
        val = 1337
        matrix.set_item(0, rows - 1, val)

        matrix.transpose()

        self.assertEquals(val, matrix.get_item(rows - 1, 0))


    def test_should_contain_1337_in_last_row_after_transpose(self):
        cols = 100
        rows = 1
        matrix = Matrix(cols, rows, 1)
        val = 1337
        matrix.set_item(cols - 1, 0, val)

        matrix.transpose()

        self.assertEquals(val, matrix.get_item(0, cols - 1))


    def test_should_add_itself_to_other_1x1_matrix(self):
        matrix = Matrix(1, 1, 1)
        other_matrix = Matrix(1, 1, 1336)

        matrix.add(other_matrix)

        self.assertEquals(1337, matrix.get_item(0, 0))


    def test_should_add_itself_to_other_10x10_matrix(self):
        matrix = Matrix(10, 10, 1)
        other_matrix = Matrix(10, 10, 1336)

        matrix.add(other_matrix)

        self.assertEquals(1337, matrix.get_item(9, 9))


    def test_should_substract_other_1x1_matrix(self):
        matrix = Matrix(1, 1, 1338)
        other_matrix = Matrix(1, 1, 1)

        matrix.subtract(other_matrix)

        self.assertEquals(1337, matrix.get_item(0, 0))


    def test_should_substract_other_10x10_matrix(self):
        matrix = Matrix(10, 10, 1338)
        other_matrix = Matrix(10, 10, 1)

        matrix.subtract(other_matrix)

        self.assertEquals(1337, matrix.get_item(9, 9))


    def test_should_multiply_itself_by_1x1_matrix(self):
        matrix = Matrix(1, 1, 2)
        other_matrix = Matrix(1, 1, 1337)

        matrix.multiply(other_matrix)

        self.assertEquals(2 * 1337, matrix.get_item(0, 0))


    def test_should_multiply_itself_by_10x10_matrix(self):
        matrix = Matrix(10, 10, 2)
        other_matrix = Matrix(10, 10, 1337)

        matrix.multiply(other_matrix)

        self.assertEquals(2 * 1337, matrix.get_item(9, 9))
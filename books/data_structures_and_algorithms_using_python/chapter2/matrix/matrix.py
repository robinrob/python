import copy
import operator

class Matrix:

    def __init__(self, cols, rows, init_val=1):
        self.matrix = self.init_matrix(cols, rows, init_val)
        self.transposed = False


    def init_matrix(self, cols, rows, init_val=1):
        matrix = []

        for col in range(cols):
            matrix.append([init_val])

        for col in matrix:
            for row in range(rows - 1):
                col.append(init_val)

        return matrix


    def num_rows(self):
        if not self.transposed:
            return len(self.matrix[0])
        else:
            return len(self.matrix)


    def num_cols(self):
        if not self.transposed:
            return len(self.matrix)
        else:
            return len(self.matrix[0])


    def get_item(self, col, row):
        return self.matrix[col][row] if not self.transposed else self.matrix[row][col]


    def set_item(self, col, row, scalar):
        if self.transposed:
            tmp = col
            col = row
            row = tmp

        self.matrix[col][row] = scalar


    def set_all(self, scalar):
        self.on_all(self.set_item(), scalar)


    def on_all(self, f, args=[]):
        new_matrix = Matrix(self.num_cols(), self.num_rows())
        for col in range(self.num_cols()):
            for row in range(self.num_rows()):
                new_matrix.set_item(col, row, f(self.get_item(col, row), args))

        self.matrix = new_matrix.matrix


    def scale_by(self, scalar):
        self.on_all(self.scale, [scalar])
        return self


    def scale(self, element, args):
        element *= args[0]
        return element


    def transpose(self):
        self.transposed = not self.transposed


    def add(self, other_matrix):
        self.operate(other_matrix, operator.add)


    def subtract(self, other_matrix):
        self.operate(other_matrix, operator.sub)


    def multiply(self, other_matrix):
        self.operate(other_matrix, operator.mul)


    def operate(self, other_matrix, operation):
        for i in range(self.num_cols()):
            for j in range(self.num_rows()):
                self.set_item(i, j, operation(self.get_item(i, j), other_matrix.get_item(i, j)))


    def __iter__(self):
        self.next_col = 0
        self.next_row = 0

        return self


    def __next__(self):
        if self.next_row is self.num_rows():
            raise StopIteration

        val = self.get_item(self.next_col, self.next_row)

        self.next_col += 1

        if self.next_col is self.num_cols():
            self.next_col = 0
            self.next_row += 1

        return val


    def __str__(self):
        s = ''
        for element in self:
            s += str(element) + ' '

        return s
class Grid:

    def __init__(self, n_rows, n_cols):
        self.grid = []

        row = []
        for i in range(n_cols):
            row.append(False)

        for j in range(n_rows):
            self.grid.append(list(row))


    def num_rows(self):
        return len(self.grid[0])


    def num_cols(self):
        return len(self.grid)


    def configure(self, coord_list):
        for coord in coord_list:
            self.set_cell(coord[0], coord[1])


    def set_cell(self, coords):
        self.grid[coords[0]][coords[1]] = True


    def clear_cell(self, coords):
        self.grid[coords[0]][coords[1]] = False


    def is_live_cell(self, coords):
        return self.grid[coords[0]][coords[1]]


    def num_live_neighbours(self, coords):
        n_live = 0;
        x = coords[0]
        y = coords[1]

        left = max(x - 1, 0)
        right = min(x + 2, self.num_cols())
        top = min(y + 2, self.num_rows())
        bottom = max(y - 1, 0)

        for i in range(left, right):
            for j in range(bottom, top):
                if not((i is x) and (j is y)):
                    n_live += (1 if self.is_live_cell((i, j)) else 0)

        return n_live


    def num_live(self):
        n_live = 0;

        for i in range(0, self.num_cols()):
            for j in range(0, self.num_rows()):
                if self.grid[i][j]:
                    n_live += 1

        return n_live


    def __iter__(self):
        self.next_col = 0
        self.next_row = 0

        return self


    def __next__(self):
        #print("point: " + str(self.next_col) + ", " + str(self.next_row))
        if self.next_col < (self.num_cols() - 1):
            self.next_col += 1
        else:
            self.next_col = 0
            if self.next_row < (self.num_rows() - 1):
                self.next_row += 1
            else:
                raise StopIteration

        return (self.next_col, self.next_row)
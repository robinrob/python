from grid import Grid

class Algo():

    @staticmethod
    def play(grid):
        new_grid = Grid(grid.num_cols(), grid.num_rows())

        for point in grid:
            n_neighbours = grid.num_live_neighbours(point)

            if (n_neighbours is 2 or n_neighbours is 3) and grid.is_live_cell(point):
                new_grid.set_cell(point)

            elif n_neighbours is 3 and not grid.is_live_cell(point):
                new_grid.set_cell(point)

        return new_grid


from life_grid import LifeGrid

class LifeAlgo():

    @staticmethod
    def play(life_grid):
        new_grid = LifeGrid(life_grid.num_cols(), life_grid.num_rows())

        for point in life_grid:
            n_neighbours = life_grid.num_live_neighbours(point)

            if (n_neighbours is 2 or n_neighbours is 3) and life_grid.is_live_cell(point):
                new_grid.set_cell(point)

            elif n_neighbours is 3 and not life_grid.is_live_cell(point):
                new_grid.set_cell(point)

        return new_grid


import settings as settings

class Drawer:

    @staticmethod
    def draw(grid, live=settings.LIVE, dead=settings.DEAD):
        border = ""
        for i in range(0, grid.num_cols()):
            border += "-"

        print("live: " + str(grid.num_live()))
        print(border)

        for i in range(0, grid.num_rows()):
            line = ""
            for j in range(0, grid.num_cols()):
                cell = (j, i)
                if grid.is_live_cell(cell):
                    line += live
                else:
                    line += dead

            print(line)

        print(border)
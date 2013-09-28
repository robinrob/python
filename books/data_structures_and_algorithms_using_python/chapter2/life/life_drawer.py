class LifeDrawer:

    @staticmethod
    def draw(life_grid):
        border = ""
        for i in range(0, life_grid.num_cols()):
            border += "-"

        print("live: " + str(life_grid.num_live()))
        print(border)

        for i in range(0, life_grid.num_rows()):
            line = ""
            for j in range(0, life_grid.num_cols()):
                cell = (j, i)
                if life_grid.is_live_cell(cell):
                    line += "*"
                else:
                    line += " "

            print(line)

        print(border)
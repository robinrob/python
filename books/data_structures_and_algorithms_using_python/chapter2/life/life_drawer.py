import life_settings as settings

class LifeDrawer:

    @staticmethod
    def draw(life_grid, live=settings.LIVE, dead=settings.DEAD):
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
                    line += live
                else:
                    line += dead

            print(line)

        print(border)
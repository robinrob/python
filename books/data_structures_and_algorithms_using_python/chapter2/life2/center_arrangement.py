class CenterArrangement:

    def __init__(self, cells):
        self.cells = cells


    def arrange(self, width, height):
        new_cells = []
        for cell in self.cells:
            x = int(width / 2) + cell[0]
            y = -1 * (int(height / 2) + cell[1])
            new_cells.append((x, y))

        self.cells = new_cells
        return new_cells

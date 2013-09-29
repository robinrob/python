class LifeConfig:

    def __init__(self, width, height):
        self.width = width
        self.height = height


    def center(self, cells):
        new_cells = []
        for cell in cells:
            x = int(self.width / 2) + cell[0]
            y = -1 * (int(self.height / 2) + cell[1])
            new_cells.append((x, y))

        return new_cells


    def grid(self, size):
        cells = []
        for i in range(size):
            for j in range(size):
                cells.append((i, j))

        return self.center(cells)

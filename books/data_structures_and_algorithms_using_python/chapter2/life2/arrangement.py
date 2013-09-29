class Arrangement:

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


    def line(self, size):
        cells = []
        sign = 1

        for i in range(size):
            if (i % 2):
                cells.append((int(i / 2), 0))
            else:
                cells.append((int(- i / 2), 0))

        return self.center(cells)

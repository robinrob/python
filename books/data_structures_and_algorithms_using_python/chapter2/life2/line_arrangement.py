from cell_arrangement import CellArrangement
from center_arrangement import CenterArrangement

class LineArrangement(CellArrangement):

    def __init__(self, size):
        self.size = size


    def arrange(self, width, height):
        cells = []
        sign = 1

        for i in range(self.size):
            if (i % 2):
                cells.append((int(i / 2), 0))
            else:
                cells.append((int(- i / 2), 0))

        return CenterArrangement(cells).arrange(width, height)
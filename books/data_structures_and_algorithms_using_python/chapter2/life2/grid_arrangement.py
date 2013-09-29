from cell_arrangement import CellArrangement
from center_arrangement import CenterArrangement

class GridArrangement(CellArrangement):

    def __init__(self, size):
        self.size = size


    def arrange(self, width, height):
        cells = []
        for i in range(self.size):
            for j in range(self.size):
                cells.append((i, j))

        return CenterArrangement(cells).arrange(width, height)
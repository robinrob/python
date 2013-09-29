from cell_arrangement import CellArrangement
from grid_arrangement import GridArrangement
from line_arrangement import LineArrangement
from center_arrangement import CenterArrangement


LIVE = chr(169)
DEAD = " "


#CELLS = [(-1, 1), (0, 1), (1, 1)]

# Qaudruple dual-oscillator
#CELLS = [(-1, 1), (0, 1), (1, 1),
#         (-1, 0), (0, 0), (1, 0),
#         (-1, -1), (0, -1), (1, -1)]


# This one reaches a stable structure after 3 turns!
#CELLS = [(0, 1), (1, 1),
#         (1, 0), (2, 0)]


# Wow, four stable structures
#CELLS = [(-2, 1), (-1, 1), (0, 1), (1, 1), (2, 1),
#         (-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0),
#         -2, -1), (-1, -1), (0, -1), (1, -1), (2, -1)]

#STARTING_ARRANGEMENT = CenterArrangement(CELLS)


#STARTING_ARRANGEMENT = GridArrangement(10)
STARTING_ARRANGEMENT = LineArrangement(10)
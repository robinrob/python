LIVE = chr(169)
DEAD = " "


#CONFIG = [(-1, 1), (0, 1), (1, 1)]

# Qaudruple dual-oscillator
CONFIG = [(-1, 1), (0, 1), (1, 1),
          (-1, 0), (0, 0), (1, 0),
          (-1, -1), (0, -1), (1, -1)]


# This one reaches a stable structure after 3 turns!
#CONFIG = [(0, 1), (1, 1),
#                          (1, 0), (2, 0)]


# Wow, four stable structures
CONFIG = [
    (-2, 1), (-1, 1), (0, 1), (1, 1), (2, 1),
    (-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0),
    (-2, -1), (-1, -1), (0, -1), (1, -1), (2, -1)]
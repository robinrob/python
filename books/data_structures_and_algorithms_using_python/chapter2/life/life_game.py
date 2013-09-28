import time

from life_drawer import LifeDrawer

class LifeGame:

    def __init__(self, life_grid, life_algo):
        self.life_grid = life_grid
        self.life_algo = life_algo


    def play(self, n_turns, delay):
        for turn in range(0, n_turns):
            print("turn: " + str(turn), end=" ")
            LifeDrawer.draw(self.life_grid)
            if turn < (n_turns - 1):
                time.sleep(delay)
                self.life_grid = self.life_algo.play(self.life_grid)

        exit(0)

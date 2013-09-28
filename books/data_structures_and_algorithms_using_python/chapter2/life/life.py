#!/usr/bin/python3

import sys
import argparse

from life_grid import LifeGrid
from life_algo import LifeAlgo
from life_game import LifeGame

parser = argparse.ArgumentParser(description='Play a game of Life.')

parser.add_argument('width', metavar='width', type=int,
                    help='width of world')

parser.add_argument('height', metavar='height', type=int,
                    help='height of world')

parser.add_argument('turns', metavar='turns', type=int,
                    help='number of turns')

parser.add_argument('delay', metavar='delay', type=float,
                    help='delay between turns')

args = parser.parse_args();

grid = LifeGrid(args.width, args.height)

me = (int(args.width / 2), int(args.height / 2))
cells = [
        #me,
        (int(args.width / 2) + 1, int(args.height / 2)),
        (int(args.width / 2) - 1, int(args.height / 2))
        #(int(args.width / 2), int(args.height / 2) - 1),
        #(int(args.width / 2) + 1, int(args.height / 2) + 1),
        #(int(args.width / 2) + 1, int(args.height / 2) - 1),
        #(int(args.width / 2) - 1, int(args.height / 2) - 1),
        #(int(args.width / 2) - 1, int(args.height / 2) + 1)
        ]

for cell in cells:
    grid.set_cell(cell)

game = LifeGame(grid, LifeAlgo())

game.play(args.turns, args.delay)
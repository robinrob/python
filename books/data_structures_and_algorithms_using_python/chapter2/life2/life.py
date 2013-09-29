import argparse

import settings
from grid import Grid
from algo import Algo
from game import Game

parser = argparse.ArgumentParser(description='Play a game of .')

parser.add_argument('width', metavar='width', type=int,
                    help='width of world')

parser.add_argument('height', metavar='height', type=int,
                    help='height of world')

parser.add_argument('turns', metavar='turns', type=int,
                    help='number of turns')

parser.add_argument('delay', metavar='delay', type=float,
                    help='delay between turns')

args = parser.parse_args();

grid = Grid(args.width, args.height)

game = Game(grid, Algo)
game.configure(settings.STARTING_ARRANGEMENT.arrange(args.width, args.height))
game.play(args.turns, args.delay)
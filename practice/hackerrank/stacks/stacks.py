#!/usr/bin/env python

import sys


def _play(x, a, b):
    a.reverse()
    b.reverse()

    removed = []
    total = 0
    score = 0
    while len(a) > 0 and (total + a[-1]) <= x:
        a_top = a.pop()
        removed.append(a_top)
        total += a_top
        score += 1

    while len(b) > 0:
        total += b.pop()
        if total > x:
            if len(removed) > 0:
                total -= removed.pop()
            else:
                break
        else:
            score += 1

    return score


if __name__ == "__main__":
    g = int(raw_input().strip())
    games = []
    for a0 in xrange(g):
        n,m,x = raw_input().strip().split(' ')
        n,m,x = [int(n),int(m),int(x)]
        a = map(int, raw_input().strip().split(' '))
        b = map(int, raw_input().strip().split(' '))
        # your code goes here

        score = _play(x, a, b)
        print score

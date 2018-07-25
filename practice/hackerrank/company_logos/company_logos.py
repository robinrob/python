#!/usr/bin/env python3


import math
import os
import random
import re
import sys


if __name__ == '__main__':
    s = input()

    letter_cnts = {}
    for letter in s:
        letter_cnts[letter] = letter_cnts.setdefault(letter, 0) + 1

    for letter_cnt in sorted(
        sorted(
            map(lambda l: (l, letter_cnts[l]), letter_cnts),
            key=lambda cnt: cnt[0]
        ),
        key=lambda cnt: cnt[1],
        reverse=True
    ):
        print("{l} {c}".format(l=letter_cnt[0], c=letter_cnt[1]))
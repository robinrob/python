#!/usr/bin/env python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))


def plus_minus(a, func):
    print '%4f' % (1.0 * sum(
        map(
            func,
            arr
        )
    ) / len(a))

plus_minus(arr, lambda x: 1 if x > 0 else 0)
plus_minus(arr, lambda x: 1 if x < 0 else 0)
plus_minus(arr, lambda x: 1 if x == 0 else 0)
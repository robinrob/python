#!/usr/bin/env python

import sys


def prim_diagonal(matrix):
    return [matrix[i][i] for i in range(len(matrix))]


def sec_diagonal(matrix):
    return [matrix[n-i-1][i] for i in range(len(matrix))]


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

print abs(sum(sec_diagonal(a)) - sum(prim_diagonal(a)))
#!/usr/bin/env python

import sys


arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)


matrix = arr


def hourglass_sum(matrix, top_left):
    sum = 0
    row = top_left[0]
    col = top_left[1]

    for j in range(row, row+3):
        if j == row + 1:
            sum += matrix[j][col+1]
        else:
            sum += sum([matrix[j][i] for i in range(col, col+3)])

    return sum


hourglass_sums = [
    hourglass_sum(matrix, (j, i))
    for j in range(4)
    for i in range(4)
]

print max(hourglass_sums)
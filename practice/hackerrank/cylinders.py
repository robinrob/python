#!/usr/bin/env python

import sys


n1,n2,n3 = raw_input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = map(int,raw_input().strip().split(' '))
h2 = map(int,raw_input().strip().split(' '))
h3 = map(int,raw_input().strip().split(' '))


def _are_equal_height(heights):
    for index, height in heights.iteritems():
        if height != heights[0]:
            return False

    return True


def _get_index_of_highest(heights):
    i_of_highest = 0
    for i in heights:
        if heights[i] > heights[i_of_highest]:
            i_of_highest = i

    return i_of_highest


cylinders = [h1, h2, h3]
for cylinder in cylinders:
    cylinder.reverse()

cylinder_heights = {
    index: sum(cylinders[index])
    for index in range(len(cylinders))
}

are_equal = _are_equal_height(cylinder_heights)
if are_equal:
    max_height = cylinder_heights[0]

while not are_equal:
    index_of_highest = _get_index_of_highest(cylinder_heights)
    reduction = cylinders[index_of_highest].pop()
    cylinder_heights[index_of_highest] -= reduction

    are_equal = _are_equal_height(cylinder_heights)
    if are_equal:
        max_height = cylinder_heights[0]

print max_height
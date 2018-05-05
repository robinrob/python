#!/usr/bin/env python

arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)


def hourglasses(arr):
    glasses = 0


print sum(map(sum, hourglasses(arr)))
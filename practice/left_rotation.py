#!/usr/bin/env python


def _left_rotate(arr):
    first = arr[0]
    arr.remove(first)
    arr.append(first)


n, d = (int(i) for i in raw_input().split(' '))

arr = [i for i in (j for j in raw_input().split(' '))]

for i in range(d):
    _left_rotate(arr)

print ' '.join(arr)
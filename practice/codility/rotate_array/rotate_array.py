#!/usr/bin/env python3

from collections import deque

def rotate_array(arr, k):
    deq = deque(arr)
    deq.rotate(k)
    return list(deq)

#!/usr/bin/env python3

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def count_apples_and_oranges(start, end, apple_tree_pos, orange_tree_pos, apples, oranges):

    return (
        len([app for app in apples if (apple_tree_pos + app) >= start and (apple_tree_pos + app) <= end]),
        len([orange for orange in oranges if (orange_tree_pos + orange) >= start and (orange_tree_pos + orange) <= end])
    )

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    apples, oranges = count_apples_and_oranges(s, t, a, b, apples, oranges)
    print(apples)
    print(oranges)

    


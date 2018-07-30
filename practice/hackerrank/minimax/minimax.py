#!/usr/bin/env python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sorted_arr = sorted(arr)
    print("{min} {max}".format(
        min=sum(sorted_arr[0:4]),
        max = sum(sorted_arr[1:])
    ))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)


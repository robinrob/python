#!/usr/bin/env python

import os
import sys

#
# Complete the getTotalX function below.
#
def get_num_between(arr1, arr2):
    nums_between = []
    num = 1
    while num < max(arr2):
        if (len([e for e in arr1 if num % e == 0]) == len(arr1)) and (len([e for e in arr2 if e % num == 0]) == len(arr2)):
            nums_between.append(num)

        num += 1

    return len(nums_between)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = get_num_between(a, b)

    f.write(str(total) + '\n')

    f.close()

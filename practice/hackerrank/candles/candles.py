#!/usr/bin/env python3

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    sorted_candles = sorted(ar, reverse=True)
    max_candle = sorted_candles[0]
    num_candles = 1

    if len(sorted_candles) > 1:
        index = 1
        while index < len(sorted_candles) and sorted_candles[index] == max_candle:
            num_candles += 1
            index += 1

    return num_candles

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))
    
    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()


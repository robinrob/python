#!/usr/bin/env python3

import sys

def is_leap(year):
    leap = False
    
    leap = (year % 4 == 0) and ((year % 100 > 0) or ((year % 100 == 0) and (year % 400 == 0)))
    
    return leap


if __name__ == "__main__":
    print(str(is_leap(int(sys.argv[1]))))
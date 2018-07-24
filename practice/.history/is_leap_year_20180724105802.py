#!/usr/bin/env python


def is_leap(year):
    leap = False
    
    leap = (year % 4 == 0) and ((year % 100 == 1) or ((year % 100 == 0) and (year % 400 == 0)))
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else
            leap = True
    
    return leap


if __name__ == "main":
    print(str(is_leap(423))
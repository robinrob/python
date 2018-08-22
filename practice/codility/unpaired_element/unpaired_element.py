#!/usr/bin/env python3

def unpaired_element(arr):
    cnts = {}
    
    for item in arr:
        cnts[item] = cnts.setdefault(item, 0) + 1

    return list(filter(lambda x: x[1] % 2 == 1, cnts.items()))[0][0]
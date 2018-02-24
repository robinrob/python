#!/usr/bin/env python

import sys


def _calc(heights):
    max_area = 0
    for height in heights:
        max_area = max(max_area, _get_area(height, heights))

    return max_area


def _get_area(first_height, heights):
    area = 0
    max_area = area
    for height in heights:
        if height >= first_height:
            area += first_height
        else:
            max_area = max(max_area, area)
            area = 0

    return max_area

if __name__ == "__main__":
    n = int(raw_input().strip())
    heights = map(int, raw_input().strip().split(' '))

    print _calc(heights)
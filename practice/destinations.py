#!/usr/bin/env python

from itertools import groupby

# Complete the function below.


def  OutputMostPopularDestination( count):
    destination_counts = {}
    for i in range(_count):
        destination = raw_input().strip()
        destination_counts[destination] = destination_counts.get(destination, 0) + 1

    most_popular = sorted(
        destination_counts.keys(),
        key=lambda key: destination_counts[key]
    )[-1]

    print most_popular


_count = int(raw_input());

OutputMostPopularDestination(_count);
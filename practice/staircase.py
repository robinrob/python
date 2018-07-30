#!/usr/bin/env python


def StairCase(n):
    for i in range(n):
        print('%{n}s'.format(n=n) % ('#' * (i + 1)))


StairCase(10)
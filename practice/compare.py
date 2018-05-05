#!/usr/bin/env python

import sys


def compare(a, b):
    return 1 if a > b else 0


def solve(*args):
    num_args = len(args)
    bob_args = args[0:num_args/2]
    alice_args = args[num_args / 2:]

    bob = sum(
        map(compare, bob_args, alice_args)
    )

    alice = sum(
        map(compare, alice_args, bob_args)
    )

    return bob, alice

a0,a1,a2 = raw_input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = raw_input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)

print " ".join(map(str, result))

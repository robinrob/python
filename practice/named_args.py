#!/usr/bin/env python

def takes_args(x, y="blah"):
    print("x: " + str(x))
    print("y: " + str(y))


takes_args(y="works!", x="this")

print("and")

takes_args("this", "works!")
#!/usr/bin/env python3

from robinset import RobinSet

a = RobinSet()
for i in range(0, 10):
    a.add(i)

b = RobinSet()
for i in range(5, 15):
    b.add(i)

print("%-15s" % "a: " + str(a))
print("%-15s" % "b: " + str(b))
print("%-15s" % "union: " + str(a.union(b)))
print("%-15s" % "interset: " + str(a.intersect(b)))
print("%-15s" % "difference: " + str(a.difference(b)))
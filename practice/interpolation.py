#!/usr/bin/env python3

print("{} {}!".format("Hello", "World"))
print("{} {} {} {}!".format("Hello", "World", 2, "times"))
print("{0} {0} {1}!".format("Hello", "World"))
print("{} {} {:d} {}!".format("Hello", "World", 0xFF, "times"))
print("{} {} {:x} {}!".format("Hello", "World", 255, "times"))
print("{} {} {:o} {}!".format("Hello", "World", 255, "times"))

print()
msg = "Hello at last!"
print(f"{msg}")
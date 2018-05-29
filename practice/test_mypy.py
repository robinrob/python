#!/usr/bin/env python3


def typed_func(x: int):
    print(int)

typed_func('a')


class TypedObject:
    def __init__(self, needs_an_int: int):
        print(needs_an_int)

TypedObject('a')
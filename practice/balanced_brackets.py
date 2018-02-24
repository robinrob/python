#!/usr/bin/env python


class Stack:

    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        item = self.data[-1]
        self.data.remove(item)
        return item

    def has_next(self):
        return len(self.data) > 0


def _are_balanced(str):
    stack = Stack()

    for char in str:
        if char in ['{', '(', '[', '}', ')', ']']:
            stack.push(char)

    while stack.has_next():
        item = stack.pop()


t = int(raw_input().strip())
for a0 in xrange(t):
    s = raw_input().strip()

    _are_balanced(s)
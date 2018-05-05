#!/usr/bin/env python

import sys


def _is_balanced(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) > 0:
                last = stack[-1]
                if last == '(':
                    stack.pop()
            else:
                return False

    return True



t = int(raw_input().strip())
for a0 in xrange(t):
    s = raw_input().strip()

    print 'YES' if _is_balanced(s) else 'NO'
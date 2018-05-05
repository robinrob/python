#!/usr/bin/env python

import sys


def _is_balanced(s):
    stack = []
    for char in s:
        if char in ['(', '{', '[']:
            stack.append(char)

        elif char == ')' and len(stack) > 0 and stack[-1] == '(':
            stack.pop()

        elif char == '}' and len(stack) > 0 and stack[-1] == '{':
            stack.pop()

        elif char == ']' and len(stack) > 0 and stack[-1] == '[':
            stack.pop()

        else:
            return False

    return len(stack) == 0

t = int(raw_input().strip())
for a0 in xrange(t):
    s = raw_input().strip()

    print 'YES' if _is_balanced(s) else 'NO'
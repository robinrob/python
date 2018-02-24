#!/usr/bin/env python


def _query(strs, query):
    ans = sum([
        1 for s in strs if query == s
    ])
    print str(ans)


n = int(raw_input())
strs = []
for i in range(n):
    strs.append(raw_input())

q = int(raw_input())
for i in range(q):
    _query(strs, raw_input())
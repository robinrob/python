#!/usr/bin/env python


n, m = (int(i) for i in raw_input().split(' '))

arr = [0] * n


for i in range(0, m):
    a, b, k = (int(i) for i in raw_input().split(' '))

    arr[a-1] += k
    if (b+1) <= n:
        arr[b] -= k

mx = 0
x = 0
for num in arr:
    x += num
    mx = max(mx, x)

print mx

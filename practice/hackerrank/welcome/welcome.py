#!/usr/bin/env python3


if __name__ == '__main__':
    n, m = map(int, input().split(' '))

    for line_num in range(n//2):
        num_bars = (2 * (line_num+1)) - 1
        line = (".|." * num_bars)
        justification = m / 2
        line = line.center(m, "-")
        print(line)

    print("WELCOME".center(m, "-"))

    for line_num in range(n//2):
        num_bars = (2 * (n // 2 - line_num)) - 1
        line = (".|." * num_bars)
        justification = m / 2
        line = line.center(m, "-")
        print(line)
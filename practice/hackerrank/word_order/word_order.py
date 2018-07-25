#!/usr/bin/env python3

from collections import OrderedDict

if __name__ == "__main__":
    n = int(input())

    word_cnts = OrderedDict()
    for i in range(n):
        word = input()

        word_cnts[word] = word_cnts.setdefault(word, 0) + 1

    print(len(word_cnts.keys()))
    print(" ".join(map(str, word_cnts.values())))
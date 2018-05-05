#!/usr/bin/env python


def query_1(seqs, last_ans, x, y):
    _get_seq(seqs, last_ans, x).append(y)


def query_2(seqs, last_ans, x, y):
    seq = _get_seq(seqs, last_ans, x)
    y_mod_size = y % len(seq)
    last_ans = seq[y_mod_size]
    print last_ans
    return last_ans


def _get_seq(seqs, last_ans, x):
    index = (x ^ last_ans) % n
    return seqs[index]


n, q = (int(i) for i in raw_input().split(' '))

sequencies = [
    [] for i in range(n)
]

last_answer = 0

input = raw_input()
while input is not None:
    query_type, x, y = (int(i) for i in input.split(' '))
    if query_type == 1:
        query_1(sequencies, last_answer, x, y)
    elif query_type == 2:
        last_answer = query_2(sequencies, last_answer, x, y)

    try:
        input = raw_input()
    except EOFError:
        input = None
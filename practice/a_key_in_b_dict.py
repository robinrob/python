#!/usr/bin/env python


a = {'one': 1, 'two': 2}

b = {'two': 3, 'three': 4}

for key in a:
    if key in b:
        word = 'also'
    else:
        word = 'NOT'

    print "'{key}' in a is {word} in b".format(key=key, word=word)

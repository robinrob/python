#!/usr/bin/env python

a = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

for key in a:
    print key

print

for key in a.keys():
    print key

for key, value in a.iteritems():
    print 'key: {var}'.format(var=key)
    print 'value: {var}'.format(var=value)
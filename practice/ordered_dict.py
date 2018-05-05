#!/usr/bin/env python

from collections import OrderedDict
from copy import copy

template = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}


def print_dict(dic):
    for key, value in dic.iteritems():
        print 'key: {var}'.format(var=key)


a = copy(template)
print_dict(a)
print

b = OrderedDict(template)
print_dict(b)
print

c = OrderedDict({})
c['one'] = 1
c['two'] = 2
c['three'] = 3
c['four'] = 4
c['five'] = 5

print_dict(c)
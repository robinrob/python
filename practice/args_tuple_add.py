#!/usr/bin/env python

def hello(*args):
    puts(*(args + (4,)))


def puts(*args):
    print 'args: {var}'.format(var=args)




hello(1,2,3)

a=[1,2,3]
hello(*a)

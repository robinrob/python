#!/usr/bin/env python

from termcolor import colored

print colored('type:', 'green')
print type(Exception)

# Used for reflection
print colored('dir:', 'green')
print dir(Exception)

print colored('id:', 'green')
print id(Exception)

print colored('getattr:', 'green')
print getattr(Exception, 'message')

print colored('hasattr:', 'green')
print hasattr(Exception, 'message')

print colored('globals:', 'green')
print globals()

print colored('locals:', 'green')
print locals()

print colored('callable:', 'green')
print callable(Exception)

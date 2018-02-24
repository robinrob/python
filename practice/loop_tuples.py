#!/usr/bin/env python

name = 'i am a (prick)/(cunt)/(tosser) full stop'
print 'name: {var}'.format(var=name)

replacements = [
    ('(', '-'),
    (')', '-'),
    ('/', '.')
]

for replacement in replacements:
    print 'replacement: {var}'.format(var=replacement)
    name = name.replace(*replacement)

print 'name: {var}'.format(var=name)
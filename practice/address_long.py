#!/usr/bin/env python

import sys

address = sys.argv[1]

parts = address.split(' ')

try:
    house_number = int(parts[0])

    street = parts[1:-1]

    for street_part in street:
        assert street_part.istitle() and street_part.isalpha()

    print 'Valid address!'

except Exception as e:
    print 'Invalid address'



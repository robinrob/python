#!/usr/bin/env python

import sys, re

address = sys.argv[1]

regex = re.compile('\A[0-9]+ ([A-Z][a-z]+\ ?)+\Z')
res = regex.match(address)

if hasattr(res, 'group'):
    print 'Valid address!'
    
else:
    print 'Invalid address'


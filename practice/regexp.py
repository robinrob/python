#!/usr/bin/env python

import re


p = re.compile("rn*")

m = p.match("rrrrobinnn!?")

if hasattr(m, 'group'):
    print(m.group())



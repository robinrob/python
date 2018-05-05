#!/usr/bin/env python

import pydash


a = [1, 2, 3]

b = 3

value = pydash.contains(a, b)

import simplejson as simplejson; print 'value: {json}'.format(json=simplejson.dumps(value, indent=4))


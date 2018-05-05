#!/usr/bin/env python

import pydash


a = [1, 2, 3]

b = [2, 3]

value = pydash.union(a, b)

import simplejson as simplejson; print 'value: {json}'.format(json=simplejson.dumps(value, indent=4))


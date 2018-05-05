#!/usr/bin/env python

from copy import copy

a = {'one': 1}
b = {'two': 2}

a.update(b)

import simplejson as simplejson; print 'a: {json}'.format(json=simplejson.dumps(a, indent=4))

b['two'] = 3

import simplejson as simplejson; print 'a: {json}'.format(json=simplejson.dumps(a, indent=4))

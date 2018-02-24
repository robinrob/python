#!/usr/bin/env python

def print_list(list):
	for item in list:
		print(item)

list1 = ["Ro.bin", "S.mith", "is", "fu.ll", "o.f.", "d.o.t.s!"]
list2 = [word.replace(".", "") for word in list1]
print_list(list2)



list = [
	{
		'a': 1,
		'b': 2
	},
	{
		'a': 3,
		'b': 4
	},
	{
		'a': 5,
		'b': 6
	}
]

import simplejson as simplejson; print 'list1: {json}'.format(json=simplejson.dumps(list1, indent=4))

list2 = [item['a'] for item in list]

import simplejson as simplejson; print 'list2: {json}'.format(json=simplejson.dumps(list2, indent=4))
import simplejson as simplejson; print 'list1: {json}'.format(json=simplejson.dumps(list1, indent=4))
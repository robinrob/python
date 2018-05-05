#!/usr/bin/env python


class Obj1:

    def __init__(self):
        pass

    def hello(self):
        print 'hello'



class Obj2(object):
    def hello(self):
        print 'hello'



class Obj3:
    def hello(self):
        print 'hello'

Obj1().hello()
Obj2().hello()
Obj3().hello()

cls = Obj1().__class__.__name__
print 'cls: {var}'.format(var=cls)
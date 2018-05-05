#!/usr/bin/env python


class Obj:
    def __init__(self):
        pass

    def hello(self):
        print "hello"


class Obj2:
    def __init__(self):
        pass

    def hello(self):
        print "HELLO"


def meth(obj=Obj()):

    obj.hello()



meth()
meth(obj=Obj2())

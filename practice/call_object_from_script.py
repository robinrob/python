#!/usr/bin/env python


class TestObj:
    def __init__(self):
        pass


    def hello(self, arg, keyword_arg=''):
        print 'arg: {arg}, keyword_arg: {keyword_arg}'.format(arg=arg, keyword_arg=keyword_arg)


def call_obj():
    TestObj().hello('Hello', 'World')



call_obj()



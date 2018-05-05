#!/usr/bin/env python

import inspect


class Obj:

    def called(self):
        stack = inspect.stack()
        the_class = stack[1][0].f_locals["self"].__class__
        the_method = stack[1][0].f_code.co_name
        print("I was called by {}.{}()".format(str(the_class), the_method))


    def caller(self):
        self.called()


Obj().caller()
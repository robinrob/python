#!/usr/bin/env python


def wrapper(some_func):
    def inner(*args, **kwargs):
        print str(some_func(*args, **kwargs) + 1)

    return inner


@wrapper
def foo(num):
    return num



foo(2)


class Obj:

    def __init__(self, disabled=False):
        self.disabled = disabled


    def wrapper(some_func):
        def inner(self, *args, **kwargs):
            if not self.disabled:
                print str(some_func(self, *args, **kwargs) + 1)

        return inner


    @wrapper
    def foo(self, num):
        return num



Obj(disabled=True).foo(2)



import logging
import traceback


logger = logging.getLogger('test')
logger.setLevel(logging.INFO)


console_handler = logging.StreamHandler()
console_handler.setLevel(level=logging.DEBUG)
console_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
logger.addHandler(console_handler)


class Logger:

    def __init__(self, disabled=False):
        self.logger = logging.getLogger('test')
        self.disabled = disabled


    @staticmethod
    def log(log_func):
        def wrapper(self, msg=''):
            if not self.disabled:
                log_func(str(msg))

        return wrapper


    @staticmethod
    def _log(log_func):
        def wrapper(self, msg=''):
            if not self.disabled:
                log_func(str(msg))

        return wrapper


    def info(self, *args, **kwargs):
        Logger._log(self.logger.info)(self, *args, **kwargs)


    def error(self, msg, err=None):
        Logger._log(self.logger.error)(self, '{msg}: {trace}'.format(msg=msg, trace=traceback.format_exc(err)))



Logger().info('test')
try:
    blah
except NameError as e:
    Logger().error('test')



class Logger2:

    def __init__(self, disabled=False):
        self.logger = logging.getLogger('test')
        self.disabled = disabled


    def log(log_func):
        def wrapper(self, msg=''):
            if not self.disabled:
                log_func(self, msg)

        return wrapper


    @log
    def info(self, msg=''):
        self.logger.info(str(msg))


    @log
    def error(self, msg=''):
        self.logger.error(str(msg))


Logger2().info('test')
Logger2().error('test')




class Obj2:

    def __init__(self):
        pass

    def do(self, msg):
        print msg


Obj2().do()
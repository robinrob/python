#!/usr/bin/env python3

from enum import Enum

from operator import attrgetter


class MyEnum(Enum):
    one = '1'
    two = '2'
    three = '3'


enum = MyEnum.one
print('enum: %s' % enum)

val = MyEnum.one.value
print('val: %s' % val)

name = MyEnum('1').name
print('name: %s' % name)

enum = getattr(MyEnum, name)
print('enum: %s' % enum)

from operator import attrgetter
enum_list = list(map(attrgetter('value'), MyEnum))
print('enum_list: %s' % enum_list)

one = MyEnum.one
res = (one.value == '1')
print('res: %s' % res)


class CustomEnumType(Enum):
    one = '1'
    two = '2'
    three = '3'


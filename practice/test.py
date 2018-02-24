#!/usr/bin/env python3

# str = b'\xF09D849E'.encode('utf8')
# print('str: %s' % str)

str = chr(int('f09d849e', 8)).encode('utf-8')
print('str: %s' % str)
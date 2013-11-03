#!/usr/bin/env python3

import copy

from robnarray import RobNArray

# arr = RobNArray(1, 2, 3, 4, 5)
# 
# print(str(len(arr)))
# 
# arr.clear(5)
# 
# print(str(arr.get_item(0, 0, 0, 0)))
# 
# arr.add_inner_dimension(6, 6)
# 
# print(str(arr.get_item(0, 0, 0, 0, 0)))
# 
# arr.add_outer_dimension(6, 6)
# 
# print(str(arr.get_item(0, 0, 0, 0, 0, 0)))
#


# t = ()
# for i in range(10):
#     t += (0,)
#         
# print(str(t))


def func_tup(*t):
    val = t
    if type(t) is tuple:
        val = *t
    print("tuple: " + str(val))
    print("list: " + str(list(val)))
    

func_tup(1, 2, 3)
func_tup((1, 2, 3))
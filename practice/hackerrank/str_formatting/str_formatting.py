#!/usr/bin/env python3


# def print_formatted(number):
#     # your code goes here
    
#     justification = len(bin(number)) - 1
#     for i in range(1, number+1):
#         print("".join([
#             str(ver[2:]).rjust(justification)
#             for ver in ["de"+str(i), oct(i), hex(i), bin(i)]
#         ])[1:])

if __name__ == '__main__':
    n = int(input())
    width = len("{0:b}".format(n))
    for i in range(1,n+1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))
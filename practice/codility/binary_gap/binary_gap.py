#!/usr/bin/env python3


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def binary_gap(N):
    # write your code in Python 3.6
    
    binary = list(bin(N)[2:])
    
    max_sequence = 0
    sequence = 0
    for digit in binary:
        if digit == '1':
            if sequence > max_sequence:
                max_sequence = sequence
            sequence = 0
        else:
            sequence += 1

    return max_sequence
            

if __name__ == '__main__':
        print(binary_gap(int(input())))
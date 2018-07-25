#!/usr/bin/env python3

from cube_stacker import can_stack_cubes

if __name__ == "__main__":
    num_test_cases = int(input())

    for _ in range(num_test_cases):
        num_cubes = int(input())
        cubes = map(int, input().split(" "))
        
        print("Yes" if can_stack_cubes(cubes) else "No")
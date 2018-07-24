#!/usr/bin/env python3

def do_command(nums, command):
    parts = command.split(" ")

    if parts[0] == "insert":
        pos = int(parts[1])
        num = int(parts[2])

        nums[pos] = num

    return nums


if __name__ == '__main__':
    N = int(input())

    nums = []
    for i in range(N):
        command = input()
        nums = do_command(nums, command)

    print(nums)

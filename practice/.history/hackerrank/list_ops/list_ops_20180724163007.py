#!/usr/bin/env python3

def do_command(list, command):
    if "insert" in command:
        parts = command.split(" ")
        pos = parts[0]
        num = parts[1]

        list[pos] = num

    return list


if __name__ == '__main__':
    N = int(input())

    nums = []
    for i in range(N):
        command = input()
        nums = do_command(nums, command)

    print nums

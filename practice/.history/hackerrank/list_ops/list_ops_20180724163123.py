#!/usr/bin/env python3

def do_command(list, command):
    parts = command.split(" ")

    if parts[0] == "insert":
        pos = int(parts[1])
        num = int(parts[2])

        list[pos] = num

    return list


if __name__ == '__main__':
    N = int(input())

    nums = []
    for i in range(N):
        command = input()
        nums = do_command(nums, command)

    print(nums)

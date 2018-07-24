#!/usr/bin/env python3

def do_command(nums, command):
    parts = command.split(" ")
    action = parts[0]

    if action == "insert":
        index = int(parts[1])
        num = int(parts[2])

        nums.insert(index, num)

    elif action == "print":
        print(nums)

    elif action == "remove":
        index = int(parts[1])

        nums.remove(index)

    elif action == "append":
        num = int(parts[1])

        nums.append(num)

    return nums


if __name__ == '__main__':
    N = int(input())

    nums = []
    for i in range(N):
        command = input()
        nums = do_command(nums, command)

    print(nums)

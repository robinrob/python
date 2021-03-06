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
        if len(nums) > 0:
            index = int(parts[1])

            nums.remove(index)

    elif action == "append":
        num = int(parts[1])

        nums.append(num)

    elif action == "sort":
        nums.sort()

    elif action == "pop":
        if len(nums) > 0:
            nums.pop()

    elif action == "reverse":
        nums.reverse()

    return nums


if __name__ == '__main__':
    N = int(input())

    nums = []
    for i in range(N):
        command = input()
        do_command(nums, command)

#!/usr/bin/env python3

from collections import deque

def do_command(deque, command):
    parts = command.split()
    action = parts[0]

    if action == "append":
        item = parts[1]
        deque.append(item)

    elif action == "appendleft":
        item = parts[1]
        deque.appendleft(item)
    
    elif action == "pop":
        deque.pop()

    elif action == "popleft":
        deque.popleft()


if __name__ == "__main__":
    n = int(input())

    deque = deque()
    for _ in range(n):
        command = input()
        do_command(deque, command)

    print(" ".join(map(str, deque)))
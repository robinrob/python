from collections import deque

def can_stack_cubes(cubes):
    cubes = deque(cubes)
    stack = []

    if len(cubes) <= 2:
        return True

    else:
        while len(cubes) > 0:
            if cubes[0] >= cubes[-1]:
                pop_left = True
                next_cube = cubes[0]
            else:
                pop_left = False
                next_cube = cubes[-1]

            if len(stack) == 0 or next_cube <= stack[-1]:
                if pop_left:
                    stack.append(cubes.popleft())
                else:
                    stack.append(cubes.pop())

            else:
                return False

    return True
#!/usr/bin/env python3

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    scores = sorted(set([student[1] for student in students]))
    [print(student[0]) for student in sorted([s for s in students if s[1] == scores[1]])]

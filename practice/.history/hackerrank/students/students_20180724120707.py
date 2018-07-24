#!/usr/bin/env python3

if __name__ == '__main__':
    students = [[]]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        print('name: %s' % name)
        students.append([name, score])
    
    scores = sorted(set([student[1] for student in students]))
    print(student[0] for student in students if student[1] == scores[-1])

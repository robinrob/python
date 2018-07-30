#!/usr/bin/env python3

#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def grade_students(grades):
    #
    # Write your code here.
    #
    for index, grade in enumerate(grades):
        if grade >= 38:
            next_multiple_of_5 = ((grade // 5) + 1) * 5

            if (next_multiple_of_5 - grade) < 3:
                grades[index] = next_multiple_of_5

    return grades

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = grade_students(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()


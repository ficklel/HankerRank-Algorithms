#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
        
        count=0
        while count<n:
            s=0
            while grades[count]-s>=0:
                s+=5  
            if grades[count]>=38:
                if s-grades[count]<3:
                    grades[count]=s 
            count+=1
        return grades 


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()

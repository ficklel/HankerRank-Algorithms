#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    arr1=[0,0,0,0,0,0]
    maxi=0
    n=arr_count
    for i in range(n) :
        for j in range(1,6) :
            if arr[i]==j :
                arr1[j]+=1
    for i in range(6) :
        if arr1[i]>maxi :
            maxi=arr1[i]
            count=i
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


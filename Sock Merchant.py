#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    arr1=[0]*n
    count=0
    for i in range(n) :
        for j in range(1,n) :
            if ar[i]==ar[j]:
                arr1[j]+=1
    for i in range(6):
        t=arr1[i]//2
        t=t
        count+=t
    return count//2     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

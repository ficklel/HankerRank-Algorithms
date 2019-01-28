#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
        t=0
        count=0
        while t<n:
            t1=t+1
            while t1<n:
                if (ar[t1]+ar[t])%k==0:
                    count+=1
                t1+=1
            t+=1
        return count            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
        maximum=scores[0]
        minimum=scores[0]
        maxi=[0,0]
        d=1
        while d<n:
            if scores[d]>maximum:
                maxi[0]+=1
                maximum=scores[d]
            if scores[d]<minimum:
                maxi[1]+=1
                minimum=scores[d]  
            d+=1    
        return maxi          

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
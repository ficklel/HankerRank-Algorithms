#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
        if x1<x2 and v1<=v2:
            return 'NO'
        if x1>x2 and v1>=v2:
            return 'NO'
        if x1<x2 and v1>v2:
            t=1
            while t<=10000:
                if x1+v1*t==x2+v2*t:
                    return 'YES'
                    break
                t+=1
            if t>=10000:
                return 'NO'
        if x1>x2 and v1<v2:
            d=1
            while d<=10000:
                if x1+v1*d==x2+v2*d:
                    return 'YES'
                    break
                d+=1
            if d>=10000:
                return 'NO'

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
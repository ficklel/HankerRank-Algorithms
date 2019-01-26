#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
        apple=[0]*m
        orange=[0]*n
        count1=0
        count2=0
        d=0
        e=0
        while d<m:
            apple[d]=a+apples[d]
            d+=1
        while e<n:
            orange[e]=b+oranges[e]
            e+=1
        d1=0
        e1=0
        while d1<m:
            if apple[d1]>=s and apple[d1]<=t:
                count1+=1
            d1+=1
        while e1<n:
            if orange[e1]>=s and orange[e1]<=t:
                count2+=1
            e1+=1
        print(count1)
        print(count2)                

            


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

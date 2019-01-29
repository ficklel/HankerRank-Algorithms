#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    t=0
    sum1=sum(bill)
    t=(sum1-bill[k])/2
    if t==b:
        print("Bon Appetit")
    else:
        d=0
        d=b-t
        print(int(d))    

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)

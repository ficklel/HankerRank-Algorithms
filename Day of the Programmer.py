#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
        #12.09.2016
        str0="12.09."
        str1="13.09."
        str2="01.09."
        if year<1918:
            if year%4==0:
                year=str(year)
                str3=str0+year
                return str3
            else:
                year=str(year)
                str3=str1+year
                return str3
        elif year ==1918:
            year=str(year)
            str3=str2+year
            return str3
        else:
            if year%400==0:
                year=str(year)
                str3=str0+year
                return str3   
            elif year%4==0 and year%100!=0:
                year=str(year)
                str3=str0+year
                return str3    
            else:
                year=str(year)
                str3=str1+year
                return str3       


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
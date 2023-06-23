import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    x=0
    y=0
    a=0
    b=-1
    for i in range(len(arr)):
        x+=arr[i][a]
        y+=arr[i][b]
        a+=1
        b-=1
    z=abs(x-y)
    return z


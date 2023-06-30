#!/bin/python3

import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    a=arr
    d=[]
    for i in range(5):
        b= a.pop(0)
        c=0
        for i in range(len(a)):
            c+= a[i]
        d.append(c)
        a.append(b)
    b=d[0]
    c=d[0]
    for i in range(len(d)):
        if d[i]>b:
            b=d[i]
        if d[i]<c:
            c=d[i]
    print(c,end=" ")
    print(b)

import math
import os
import random
import re
import sys

def getTotalX(a, b):
    x=max(a)
    y=min(b)
    r= False
    c=0
    for i in range(x,y+1):
        for j in range(len(a)):
            if i%a[j]==0:
                r = True
            else:
                r = False
                break
        if r:
            for k in range(len(b)):
                if b[k]%i==0:
                    r = True
                else:
                    r = False
                    break
        if r:
            c= c+1
    return c

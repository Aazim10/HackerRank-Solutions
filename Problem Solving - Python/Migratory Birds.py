import math
import os
import random
import re
import sys

def migratoryBirds(arr):
    s=[]
    c=[]
    l=[]
    if len(arr)>=5 and len(arr)<=(2*10**5): 
        for i in arr:
            if i not in s and i<=6:
                s.append(i)
                c.append(arr.count(i))
        d=max(c)
        e=c.count(d)
        if e>1:
            for j in range(len(c)):
                if c[j]==d:
                    l.append(s[j])
            return min(l)
        else:
            for j in range(len(c)):
                if c[j]==d:
                    return s[j]

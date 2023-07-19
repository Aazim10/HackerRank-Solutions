import os
import sys

def getMoneySpent(keyboards, drives, b):
    c=[]
    for i in keyboards:
        for j in drives:
            if (i+j)<=b:
                c.append(i+j)
    if len(c)>=1:
        return max(c)
    else:
        return -1

import math
import os
import random
import re
import sys


def compareTriplets(a, b):
    x=0
    y=0
    for i in range(len(a)):
        if a[i]>b[i]:
            x+=1
        elif a[i]<b[i]:
            y+=1
        elif a[i]==b[i]:
            pass
    return x,y



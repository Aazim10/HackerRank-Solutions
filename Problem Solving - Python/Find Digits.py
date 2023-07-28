import math
import os
import random
import re
import sys

def findDigits(n):
    s=str(n)
    d=0
    for i in range(len(s)):
        if int(s[i])!=0:
            if n%int(s[i])==0:
                d=d+1
    return d

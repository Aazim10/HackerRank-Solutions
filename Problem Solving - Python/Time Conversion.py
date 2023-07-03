import math
import os
import random
import re
import sys

def timeConversion(s):
    if s[-2]=='P':
        a= int(s[0]+s[1])
        if a==12:
            a=str(a)
            pass
        else:
            a=str(a+12)
    else:
        a= int(s[0]+s[1])
        if a==12:
            a="00"
        else:
            if a<10:
                a="0"+str(a)
            a=str(a)
            pass
    for i in range(2,8):
        a=a+s[i]
    return a

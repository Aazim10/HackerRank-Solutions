import math
import os
import random
import re
import sys

def breakingRecords(scores):
    l=scores[0]
    m=scores[0]
    r=[0,0]
    for i in range(len(scores)):
        if scores[i]>m:
            m=scores[i]
            r[0]=r[0]+ 1
        if scores[i]<l:
            l= scores[i]
            r[1]=r[1]+ 1
    return r    

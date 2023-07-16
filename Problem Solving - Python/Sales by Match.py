import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    a=0
    b=[]
    for i in ar:
        ic=0
        if i not in b:
            b.append(i)
            for j in ar:
                if i == j:
                    ic=ic+1
            if ic>0 and ic%2==0:
                a=a+(ic/2)
            elif ic>0 and ic%2!=0:
                a=a+((ic-1)/2)
            
    return int(a)

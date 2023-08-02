import math
import os
import random
import re
import sys

def minimumNumber(n, password):
    num = "0123456789"
    lc = "abcdefghijklmnopqrstuvwxyz"
    uc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sc = "!@#$%^&*()-+"
    nu=0
    l=0
    u=0
    s=0
    a=0
    b=0
    if n<6:
        a=6-n
    for i in range(n):
        if password[i] in num:
            nu=1
        if password[i] in lc:
            l=1
        if password[i] in uc:
            u=1
        if password[i] in sc:
            s=1
    if a==0 and nu==1 and l==1 and u==1 and s==1:
        return 0
    
    if nu==0:
        b=b+1
    if l==0:
        b=b+1
    if u==0:
        b=b+1
    if s==0:
        b=b+1
    
    if a>b:
        return a
    else: 
        return b

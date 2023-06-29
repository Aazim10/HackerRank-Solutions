#!/bin/python3

import math
import os
import random
import re
import sys


def plusMinus(arr):
    p=0
    n=0
    z=0
    for i in range(len(arr)):
        if arr[i]>0:
            p+=1
        elif arr[i]<0:
            n+=1
        elif arr[i]==0:
            z+=1
    print('%6f'%(p/len(arr)))
    print('%6f'%(n/len(arr)))
    print('%6f'%(z/len(arr)))
    


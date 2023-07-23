import math
import os
import random
import re
import sys

def utopianTree(n):
    h=1
    i=1
    while(i<=n):
        if i%2==0:
            h=h+1
        if i%2!=0:
            h=h*2
        i=i+1
    return h

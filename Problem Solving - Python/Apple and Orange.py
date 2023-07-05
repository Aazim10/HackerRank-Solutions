import math
import os
import random
import re
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    ac=0
    oc=0
    for i in range(len(apples)):
        h= apples[i]+a
        if h>=s and h<=t:
            ac= ac+1
    for i in range(len(oranges)):
        h= oranges[i]+b
        if h>=s and h<=t:
            oc= oc+1
    print(ac)
    print(oc)

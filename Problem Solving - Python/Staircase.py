#!/bin/python3

import math
import os
import random
import re
import sys

def staircase(n):
    c=1
    for i in range(n):
        for i in range(n-c):
            print(" ",end="")
        for i in range(c):     
            print("#",end="")
        print()
        c+=1


import math
import os
import random
import re
import sys

def angryProfessor(k, a):
    c=0
    for i in a:
        if i<=0:
            c=c+1
    if c<k:
        return "YES"
    else: 
        return "NO"

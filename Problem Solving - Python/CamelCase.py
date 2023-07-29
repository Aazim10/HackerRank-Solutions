import math
import os
import random
import re
import sys
import string

def camelcase(s):
    cap= list(string.ascii_uppercase)
    w=1
    for i in range(26):
        w= w+s.count(cap[i])
    return w

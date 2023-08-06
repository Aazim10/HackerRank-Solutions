import math
import os
import random
import re
import sys
import string

def caesarCipher(s, k):
    c=''
    low=list(string.ascii_lowercase)
    up=list(string.ascii_uppercase)
    for i in range(len(s)):
        if s[i] in low:
            g= low.index(s[i])
            c=c+low[(g+k)%26]
        elif s[i] in up:
            g= up.index(s[i])
            c=c+up[(g+k)%26]
        else:
            c=c+s[i]
    return c

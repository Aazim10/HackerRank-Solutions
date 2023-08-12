import math
import os
import random
import re
import sys
import string

def pangrams(s):
    s = s.lower()
    let=list(string.ascii_lowercase)
    b = True
    for i in range(26):
        if let[i] not in s:
            b= False
            return "not pangram"
            break
    if b:
        return "pangram"

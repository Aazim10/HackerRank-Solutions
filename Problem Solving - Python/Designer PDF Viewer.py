import math
import os
import random
import re
import sys
import string

def designerPdfViewer(h, word):
    let=list(string.ascii_lowercase)
    a=[]
    for i in range(len(word)):
        a.append(h[(let.index(word[i]))])
    b= max(a)
    c = a.index(b)
    d = int(len(word)*b)
    return d

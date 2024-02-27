import math
import os
import random
import re
import sys

def bigSorting(unsorted):
    return sorted(unsorted, key=lambda x: (len(x), x))

# This one has time issues
def bigSorting(unsorted):
    n = len(unsorted)
    for i in range(n):
        for j in range(0, n-i-1):
            if len(unsorted[j]) > len(unsorted[j+1]):
                unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]
            elif len(unsorted[j]) == len(unsorted[j+1]):
                if unsorted[j] > unsorted[j+1]:
                    unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]
    return unsorted

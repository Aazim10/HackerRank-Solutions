import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    # Write your code here
    a=candles[0]
    count=0
    for i in range(len(candles)):
        if candles[i]>a:
            a=candles[i]
    for i in range(len(candles)):
        if candles[i]==a:
            count=count+1
    return count

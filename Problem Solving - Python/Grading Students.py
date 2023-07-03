import math
import os
import random
import re
import sys

def gradingStudents(grades):
    A=[]
    for i in range(len(grades)):
        if grades[i]<38:
            A.append(grades[i])
        elif grades[i]%5==0:
            A.append(grades[i])
        elif grades[i]%5==1:
            A.append(grades[i])
        elif grades[i]%5==2:
            A.append(grades[i])
        elif grades[i]%5==3:
            A.append(grades[i]+2)
        elif grades[i]%5==4:
            A.append(grades[i]+1)
            
    return A
            

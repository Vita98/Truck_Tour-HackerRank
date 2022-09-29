#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    # Write your code here
    
    i = 0
    pivot = 0
    avPetrol = 0
    orLenght = len(petrolpumps)
    
    while len(petrolpumps) > 0:
        pump = petrolpumps.pop(0)
        avPetrol += pump[0]
        
        if avPetrol < pump[1]:
            petrolpumps.append(pump)
            avPetrol = 0
            i += 1
            pivot = i
            continue
        
        avPetrol -= pump[1]
        i += 1
    
    return pivot
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()

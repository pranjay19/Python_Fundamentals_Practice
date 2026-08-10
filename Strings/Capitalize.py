#!/bin/python3

import math 
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):

    Names_list=s.split(" ")

    for i in range(len(Names_list)):
        Names_list[i]=Names_list[i].capitalize()
        
    final_name=" ".join(Names_list)

    return final_name


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

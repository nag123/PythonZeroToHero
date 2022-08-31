#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime as dati
# Complete the time_delta function below.
def time_delta(t1, t2):
    format_time = '%a %d %b %Y %H:%M:%S %z'

    t1tm = dati.strptime(t1, format_time)
    t2tm = dati.strptime(t2, format_time)

    return str(round(abs((t1tm - t2tm).total_seconds())))

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)
        print(delta)
        #fptr.write(delta + '\n')

    #fptr.close()

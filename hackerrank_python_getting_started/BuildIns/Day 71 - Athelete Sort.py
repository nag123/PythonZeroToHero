#!/bin/python3

import math
import os
import random
import re
import sys
'''
input :::
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
0
output ::: 
1 23 12
6 5 9
7 1 0
9 9 9
10 2 5

explanation :::
Total of 5 rows and 3 ccolumns and the 6th row is sorting on the index 
'''


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    #here sorting is done based on k and since the columns are 3 you can give index of 0,1,2
    # which is first second and third element as per the example scenario
    arr.sort(key=lambda arr: arr[k])
    for x in arr:
        print(*x)

'''
Input :::
4
a a c d
2

Output :::
0.8333

Explanation

All possible unordered tuples of length 2 comprising of indices from 1 to 4 are:

(1,2)(1,3)(1,4)(2,3)(2,4)(3,4)

Out of these 6 combinations, 5 of them contain either index 1 or index 2 which are the indices that contain the letter 'a'.

Hence, the answer is 5//6.

Things to note in this ::::  Here we need to find the average of how many times 'a' occurs where i was thinking based on repeative elements,some note the condidion is on 'a'

'''
from itertools import combinations
if __name__ == '__main__':
    noofinputsfromuser = int(input())
    listofiterval = input().split()
    counter = 0
    combpositions = int(input())
    combinationvalue = list(combinations(listofiterval,combpositions))
    for i in combinationvalue:
        if('a' in i):
            counter += 1
    print(counter/len(combinationvalue))



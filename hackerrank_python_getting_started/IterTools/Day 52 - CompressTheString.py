from itertools import groupby
if __name__ == '__main__':
    for k,g in groupby(input()):
        #print("the key is ::: ",k)
        #print("the value is ::: ", list(g))
        print("The result is :::: ",(len(list(g)), int(k)), end = " ")
        print("\n")
'''
Explanation of groupby in itertool : 
Python’s Itertool is a module that provides various functions that work on iterators to produce complex iterators. 
This module works as a fast, memory-efficient tool that is used either by themselves or in combination to form iterator algebra.

Itertools.groupby()
This method calculates the keys for each element present in iterable. It returns key and iterable of grouped items.
'''
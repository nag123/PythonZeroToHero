'''
Sample input :
3 2
1 5 3
3 1
5 7

sample output :
1

Explanation :
Explanation

You gain 1 unit of happiness for elements 3 and 1 in set A.
You lose 1 unit for  in set B.
The element 7 in set B does not exist in the array so it is not included in the calculation.

Hence, the total happiness is 2 - 1 = 1.

'''
if __name__ == '__main__':
    setmandnsize = input().split(' ')
    setmsizevalues = ([int(i) for i in input().split(' ')])
    aval = set([int(i) for i in input().split(' ')])
    bval = set(list(map(int,(input().split()))))
    counter = 0
    for i in setmsizevalues:
        if(i in aval):
            counter +=1
        elif(i in bval):
            counter +=-1
        else:
            counter
    print(counter)


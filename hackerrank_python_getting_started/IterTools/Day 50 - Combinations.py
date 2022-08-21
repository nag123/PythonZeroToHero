'''
This tool returns the r length subsequences of elements from the input iterable.

Combinations are emitted in lexicographic sorted order.
 So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

Task
You are given a string S.
Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.

Input Format

A single line containing the string S and integer value k separated by a space.

Constraints
0 <k <= len(S)
The string contains only UPPERCASE characters.

Output Format

Print the different combinations of string S on separate lines.


Sample Input
HACK 2

Sample Output

A
C
H
K
AC
AH
AK
CH
CK
HK

Things I struggled : There shouldnt be a space value so filter on the space since i am using split here
making the tuple to a string and then joining in print statement
'''
from itertools import combinations
if __name__ == '__main__':
    res = list()
    word, r = input().split()
    itervalue = sorted(word)
    for i in range(int(r)+1):
        res += combinations(itervalue,i)
    print('\n'.join(''.join(tup) for tup in filter(None,res)))

'''
INPUT :
STDIN        Function
-----        --------
2            T = 2
6            blocks[] size n = 6
4 3 2 1 3 4  blocks = [4, 3, 2, 1, 3, 4]
3            blocks[] size n = 3
1 3 2        blocks = [1, 3, 2]

OUTPUT :
Yes
No

In the first test case, pick in this order: left - 4, right - 4, left - 3, right - 3, left - 2, right - 1.
In the second test case, no order gives an appropriate arrangement of vertical cubes. 3 will always come after either 1 or 2.
'''
from collections import deque
if __name__ == '__main__':
    noofiterationintotal = int(input())
    for i in range(noofiterationintotal):
        noofiterations , valuesofeachiteration = int(input()),deque(map(int,input().split()))
        copyoforiginalinputs = valuesofeachiteration.copy()
        lst = [valuesofeachiteration.popleft() if valuesofeachiteration[0] >= valuesofeachiteration[-1] else valuesofeachiteration.pop() for block in copyoforiginalinputs]
        if(lst == sorted(copyoforiginalinputs,reverse=True)):
            print("Yes")
        else:print("No")

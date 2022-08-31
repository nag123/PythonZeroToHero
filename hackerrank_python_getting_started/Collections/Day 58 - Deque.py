'''
    d = deque()
    d.append(1)
    print(d)
    d.appendleft(2)
    print(d)
    d.clear()
    print(d)
    d.extend('1')
    print(d)
    d.extendleft('234')
    print(d)
    d.count('1')
    d.pop()
    print(d)
    d.popleft()
    print(d)
    d.extend('7896')
    print(d)
    d.remove('2')
    print(d)
    d.reverse()
    print(d)
    d.rotate(4)
    print(d)

    input :
    6
append 1
append 2
append 3
appendleft 4
pop
popleft

output:
1 2
'''
from collections import deque
if __name__ == "__main__":
    N = int(input())
    d = deque()
    for i in range(N):
        ins = input().split(" ")

        if(len(ins) > 1):
            eval("d.{}({})".format(ins[0],ins[1]))
        else:
            eval("d.{}()".format(ins[0]))

    print(' '.join(map(str,d)))
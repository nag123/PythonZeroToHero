from __future__ import print_function

if __name__ == '__main__':
    n = int(input())
    tup = []
    returnresult = ""
    for i in range(n):
        tup.append(str(i+1))
    print("".join(tup))


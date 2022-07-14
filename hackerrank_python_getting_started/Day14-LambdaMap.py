cube = lambda x: x*x*x # lambda function to return cube

def fibonacci(n):
    # return a list of fibonacci numbers
    fibolist = list()
    lastvalue = 0
    ans = 0
    for i in range(n):
        if(i == 0) :
            ans = 0
        elif(i == 1) :
            ans = 1
        else:
            lastvalue = fibolist[-1]
            secondlastvalue = fibolist[-2]
            ans = secondlastvalue + lastvalue
        fibolist.append(ans)
    return fibolist
'''
0th iteration 0 = 0
1st iteration 1 = 1
2nd iteration 0+1 = 1
3rd iteration 1+1 = 2
4rd iteration 2+1 = 3
'''

if __name__ == '__main__':
    n = int(input())
    fibval = fibonacci(n)
    print(map(cube,fibval))

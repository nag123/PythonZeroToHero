from itertools import product
if __name__ == '__main__':
    '''print(list(product([1, 2, 3], repeat=2)))
    print(list(product([1,2,3],[3,4])))
    A = [[1, 2, 3], [3, 4, 5]]
    print(list(product(*A)))
    B = [[1, 2, 3], [3, 4, 5], [7, 8]]
    print(list(product(*B)))
    '''
    A = list(input().split())
    B = list(input().split())

    for v,y in product(A,B):
        s = ((int(v),int(y)))
        print(s,end=" ")


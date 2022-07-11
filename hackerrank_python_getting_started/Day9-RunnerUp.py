if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    #print(sorted(set(arr))) # [2 3 4 5]
    va = sorted(set(arr))[-2]
    print(va)
    #print(sorted(set(arr))[1])
    #print(sorted(list(set(arr)))[-2])





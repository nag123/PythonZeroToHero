if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        setAnos = int(input())
        setAVales = set(input().split())
        setBnos = int(input())
        setBvales = set(input().split())
        print(setAVales.issubset(setBvales))

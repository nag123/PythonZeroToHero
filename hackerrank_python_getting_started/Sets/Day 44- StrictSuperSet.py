if __name__ == '__main__':
    queenset = set(input().split())
    counter = 0
    n = int(input())
    for i in range(n):
        inputofsubset = set(input().split())
        if queenset.issuperset(inputofsubset):
            counter += 1
    print(counter == n)
def average(array):
    # your code goes here
    arr = set(array)
    totl = sum(arr)
    noofval = len(arr)
    return float(totl/noofval)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
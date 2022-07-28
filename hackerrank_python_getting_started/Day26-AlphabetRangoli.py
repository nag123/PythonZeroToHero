def print_rangoli(size):
    # your code goes here
    alpkeys = "abcdefghijklmnopqrstuvwxyz"
    iterator = [alpkeys[i] for i in range(n)]
    items = list(range(n))
    items = items[:-1] + items[::-1]
    for i in items:
        temp = iterator[-(i + 1):]
        rowval = temp[::-1] + temp[1:]
        print("-".join(rowval).center(n * 4 - 3, "-"))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
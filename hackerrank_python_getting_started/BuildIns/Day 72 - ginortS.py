if __name__ == "__main__":
    wordinput = input()

    low = []
    up = []
    odd = []
    even = []

    for i in wordinput:
        if i.isupper():
            up.append(i)
        elif i.islower():
            low.append(i)
        elif i.isdigit() and (int(i) % 2 != 0):
            odd.append(i)
        elif i.isdigit() and (int(i) % 2 == 0):
            even.append(i)

    low.sort()
    up.sort()
    odd.sort()
    even.sort()

    final = [low, up, odd, even]
    for i in final:
        for l in i:
            print(l, end="")
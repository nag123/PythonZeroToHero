if __name__ == "__main__":
    #Code
    try:
        print(1/0)
    except ZeroDivisionError as e:
        print("Error Code:",e)

    a = '1'
    b = '#'
    try:
        print(int(a) / int(b))
    except ValueError as v : print("Error Code:",v)

    noofusecasesfromusers = int(input())
    for i in range(noofusecasesfromusers):
        a, b = input().split()
        try:
            print(int(int(a)//int(b)))
        except ZeroDivisionError as zde: print("Error Code:",zde)
        except ValueError as ve:print("Error Code:",ve)



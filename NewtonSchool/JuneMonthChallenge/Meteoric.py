def calc(number):
    startingnum, multiplynum = number.split()
    result = int(startingnum)
    for i in range(int(multiplynum)):
        result = result * 2
    return result


if __name__ == '__main__':
    number = input()
    print(calc(number))

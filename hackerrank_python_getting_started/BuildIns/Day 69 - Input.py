def calculatepolynomial():
    if (eval(polynomial) == int(highervalue)):
        return True
    else:
        return False


if __name__ == "__main__":
    lowervalue,highervalue = input().split()
    sum = 0
    polynomial = input().replace("x",lowervalue)
    print(calculatepolynomial())





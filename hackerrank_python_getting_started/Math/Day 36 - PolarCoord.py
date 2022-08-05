import cmath
if __name__ == '__main__':
    val = input()
    print(abs(complex(val)))
    print(cmath.phase(complex(val)))
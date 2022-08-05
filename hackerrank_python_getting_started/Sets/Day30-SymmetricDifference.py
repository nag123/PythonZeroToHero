'''
TC1 :
2
-10 -10
3
-20 -20 -20


'''
if __name__ == '__main__':
    setasize = input()
    setavalues = set()
    setaval = input()
    setavalint = setaval.split()
    setavalues = list(map(int, setavalint))

    setbsize = input()
    setbvalues = set()
    setbval = input()
    setbvalint = setbval.split()
    setbvalues = list(map(int, setbvalint))

    finalresult = sorted(set(setavalues).symmetric_difference(set(setbvalues)))
    print(finalresult)

    print('\n'.join(map(str,finalresult)))
''' setbsize = input()
    setbvalues = set()
    for i in range(int(setbsize)):
        setbvalues = set(input().split())
        if (len(setbvalues) == setbsize):
            break
    setbintvals = set(map(int, setbvalues))
    finalresult = sorted(setaintvals.symmetric_difference(setbintvals))

    print('\n'.join(map(str,finalresult)))

'''
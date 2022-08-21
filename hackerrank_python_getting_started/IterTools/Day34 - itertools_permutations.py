from itertools import permutations
if __name__ == '__main__':
    inputfromuser = input()
    valofword = inputfromuser.split(" ")[0]
    perm = int(inputfromuser.split(" ")[1])
    for v in sorted(permutations(valofword,perm)):
        print(''.join(v))
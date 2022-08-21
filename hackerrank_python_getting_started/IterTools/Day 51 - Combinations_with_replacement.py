from itertools import combinations_with_replacement
if __name__ == '__main__':
    res = list()
    word, r = input().split()
    itervalue = sorted(word)
    res += combinations_with_replacement(itervalue,int(r))
    print("\n".join(''.join(tup) for tup in filter(None,res)))
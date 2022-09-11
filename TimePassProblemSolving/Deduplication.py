from collections import OrderedDict
if __name__ == "__main__":
    word = "aabccadaddpc"
    n = int(input())
    print('\n'.join(''.join(OrderedDict.fromkeys(word[i:i+n])) for i in range(0,len(word),n)))






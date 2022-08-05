def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string),k):
        subs = string[i:i+k]
        eachval = list(dict.fromkeys(subs))
        print(''.join(eachval))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
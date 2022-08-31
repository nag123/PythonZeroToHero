'''
The defaultdict tool is a container in the collections class of Python.
It's similar to the usual dictionary (dict) container, but the only difference is that
a defaultdict will have a default value if that key has not been set yet.
If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.

from collections import defaultdict

if __name__ == '__main__':

    d = defaultdict(list)
    print("defaultdict for the first time",d)
    d['python'].append("awesome")
    print("defaultdict for the second time after appending awesome value to defaultdict python key", d)
    d['something-else'].append("not relevant")
    print("defaultdict for the 3rd time after appending not relevant value to something-else key", d)
    d['python'].append("language")
    print("defaultdict for the 4th time after appending language as value to python key", d)
    for i in d.items():
        print(i)

    OUTPUT :
defaultdict for the first time defaultdict(<class 'list'>, {})
defaultdict for the second time after appending awesome to defaultdict python defaultdict(<class 'list'>, {'python': ['awesome']})
defaultdict for the 3rd time after appending not relevant to something-else defaultdict(<class 'list'>, {'python': ['awesome'], 'something-else': ['not relevant']})
defaultdict for the 4th time after appending language to python defaultdict(<class 'list'>, {'python': ['awesome', 'language'], 'something-else': ['not relevant']})
('python', ['awesome', 'language'])
('something-else', ['not relevant'])

In this challenge, you will be given 2 integers, n and m.
There are n words, which might repeat, in word group A .
There are m words belonging to word group B .
For each  words, check whether the word has appeared in group A or not.
Print the indices of each occurrence of m in group A. If it does not appear, print -1 .
INPUT :::
STDIN   Function
-----   --------
5 2     group A size n = 5, group B size m = 2
a       group A contains 'a', 'a', 'b', 'a', 'b'
a
b
a
b
a       group B contains 'a', 'b'
b
OUTPUT :::
1 2 4
3 5

Explanation

'a' appeared 3 times in positions 1,  2 and 4.
'b' appeared 2 times in positions 3 and 5.
In the sample problem, if 'c' also appeared in word group B, you would print -1.
'''

from collections import defaultdict

if __name__ == "__main__":
    A,B = map(int,input().split())
    m = defaultdict(list)

    for i in range(1,A+1):
        m[input()].append(i)
    for i in range(B):
        inval = input()
        if inval in m.keys():
            print(" ".join(map(str,m[inval])))
        else:
            print("-1")
        #print(" ".join(map(str,m.get(input(),"-1"))))


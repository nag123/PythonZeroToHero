'''
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2
Function Description

Complete the swap_case function in the editor below.

swap_case has the following parameters:

string s: the string to modify
Returns

string: the modified string
Input Format

A single line containing a string S
input : HackerRank.com presents "Pythonist 2".
output: hACKERrANK.COM PRESENTS "pYTHONIST 2".

'''
def swap_case(s):
    n = ""
    for c in s:
        if(c.islower()): n += str(c.upper())
        else:n += str(c.lower())
    return n


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
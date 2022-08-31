'''

Input Format

The first line contains the integer, n.
The next n lines each contain a word.

Output Format :
Output 2 lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.
Input :
4
bcdef
abcdefg
bcde
bcdef

output :
3
2 1 1

Explanation :
There are 3 distinct words. Here, "bcdef" appears twice in the input at the first and last positions.
 The other words appear once each.
 The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.

'''

if __name__ == "__main__":
    n = int(input())
    thewords = dict()
    for i in range(n):
        wordsfromuser = input()
        if wordsfromuser not in thewords:
            thewords[wordsfromuser] = 1
        else :
            thewords[wordsfromuser] += 1
    print(len(thewords))

    for i in thewords :
        print(thewords[i] , end = ' ')

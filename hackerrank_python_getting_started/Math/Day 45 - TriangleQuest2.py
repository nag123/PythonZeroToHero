'''
You are given a positive integer N.
Your task is to print a palindromic triangle of size N.

For example, a palindromic triangle of size  5 is:
1
121
12321
1234321
123454321

You can't take more than two lines. The first line (a for-statement) is already written for you.
You have to complete the code using exactly one print statement.

Note:
Using anything related to strings will give a score of 0.
Using more than one for-statement will give a score of 0.

Input Format
A single line of input containing the integer N.

Constraint
0 < N < 10

Output Format
Print the palindromic triangle of size N as explained above.

input
5

output
1
121
12321
1234321
123454321

Logic I have applied the logic with i as in range that is taken from input
10^1 = 10 => 10-1 = 9 => 9/9 = 1 =>1^2 => 1
10^2 = 100 => 100-1 = 99 => 99/9 = 11 =>11^2 => 121
10^3 = 1000 => 1000-1 = 999 => 999/9 = 111 =>111^2 => 12321
and so on

'''
if __name__ == '__main__':
    for i in range(1, int(input()) + 1):  # More than 2 lines will result in 0 score. Do not leave a blank line also
        print (int((10**i-1)/9)**2)
'''
This is  an interesting problem where you need to check in  a list of 5 numbers

conditions :
1. All the numbers are positive
2. Any of the number is a palindromic integer
Ex : 0 till 9 and reverse of a number is same as the number like "121" reversed is 121 again

The challenge is to solve in 3 lines ;)

5
12 9 61 5 14

Here all are positive integer numbers and 9,5 are palindromic integers since any(9,5) it is true so return is true
'''

if __name__ == "__main__":
    n = int(input())
    inputnumbers = list(map(int, input().split()))
    print(all(True if i > 0 else False for i in inputnumbers) and any(True if str(i) == str(i)[::-1] else False for i in inputnumbers))

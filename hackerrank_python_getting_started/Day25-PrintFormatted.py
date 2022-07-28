'''
Given an integer,n , print the following values for each integer i from 1 to N:

Decimal
Octal
Hexadecimal (capitalized)
Binary

Prints

The four values must be printed on a single line in the order specified above for each i from 1 to number.
Each value should be space-padded to match the width of the binary value of number
and the values should be separated by a single space.

'''
def print_formatted(number):
    # Requirement : value should be self spaced to match width of binary value of number
    padding = len(str(bin(number)))
    for i in range(1,number+1):
        D = str(i)
        B = str(bin(i)[2:])
        O = str(oct(i)[2:])
        HC = str(hex(i)[2:]).upper()
        #requirement : the values should be separated by a single space. so padding -1 , Since in decimal
        #Decimal - we are padding with -2 rjust since it takes len of binary digit  -1 padding
        print(D.rjust(padding-2)+O.rjust(padding-1)+HC.rjust(padding-1)+B.rjust(padding-1))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
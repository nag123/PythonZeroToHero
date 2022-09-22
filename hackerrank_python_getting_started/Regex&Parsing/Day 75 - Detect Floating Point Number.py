'''
input :
4
4.0O0
-1.00
+4.54
SomeRandomStuff

output:
False
True
True
False

Explanation :
4.0O0   : O is not a digit.
-1.00   : is valid.
+4.54   : is valid.
SomeRandomStuff: is not a number.
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    for N in range(int(input())):
        try:
            print(bool(float(input())))
        except:
            print(False)

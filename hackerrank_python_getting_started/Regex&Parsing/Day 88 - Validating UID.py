'''
ABCXYZ company has up to  employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

It must contain at least  uppercase English alphabet characters.
It must contain at least  digits ( 0 to 9 ).
It should only contain alphanumeric characters ( a-z ,  A-Z  &  0-9 ).
No character should repeat.
There must be exactly  characters in a valid UID.
'''
if __name__ == "__main__":
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    n = int(input())
    for i in range(n):
        uid = input()
        if len(uid) == 10 and len(set(uid)) == 10 and len([i for i in uid if i.isnumeric()]) >= 3 and len(
                [i for i in uid if i.isupper()]) >= 2 and uid.isalnum():
            print("Valid")
        else:
            print("Invalid")




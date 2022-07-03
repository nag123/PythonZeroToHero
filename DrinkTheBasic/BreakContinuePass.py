'''
BREAK : Breaks out of the current loop
CONTINUE : Ends the current execution and goes to the next iteration
PASS : This statement does nothing. It is used when a statement is required . But the program requires no action
'''

def BreakTest(arr):
    for i in arr:
        if i == 5:
            break
        print(i)
    print("END OF BREAKTEST METHOD")

arr = [1,3,4,5,7,9,15]
BreakTest(arr)

def ContinueTest(arr):
    for i in arr:
        if i == 5:
            continue
        print(i)
    print("END OF CONTINUE METHOD")

def PassTest(arr):
    for i in arr:
        if(i == 5):
            pass
        print(i)





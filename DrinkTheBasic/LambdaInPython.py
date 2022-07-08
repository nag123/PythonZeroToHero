#lambda Function : An anonymous function that can take any number of arguments, but can only have one expression.
#Syntax          : lambda arguments : expression
#Example :
x = lambda a : a+10
y = lambda a,b : a*b

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2) #passing argument to the function
print(mydoubler(11)) #passing value to the ananymous function

#test to myself - print a string
q = "Naxie  - The Best"
(lambda q: print(q))(q)

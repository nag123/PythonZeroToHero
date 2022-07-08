
#STRINGS IN PYTHON
print("Program to iterate in a string : banana")
for x in "banana":
  print(x)


#LENGTH IN STRING
print("Length in a string ::: \n ",len("banana"))

#CHECK A STRING FROM A TEXT
print("Check if a part of word present in a word :::  \n ", "na" in "banana")

#CHECK A PART OF WORD USING IF STATEMENT
print("Check a part of word present using the if statement")
phrase = "The best things in the world are free !!! "
if("free" in phrase): print("Yes ! Free is present in the text")
#checking true or false if a word is present or not
print("cool" not in phrase)
#using not in
if("expensive" not in phrase): print("Yes ! expensive is not present in the text")

print("\n\n\t************************* SLICING IN STRING *************************\n\n")
#slicing in string
print("Lets learn about slicing in string \n")
b = "Hello, Rocky!!!"
print("Example :::  Hello, Rocky!!!")
print(" \n \n we are going to taking from 2nd index to 5th index .. Indexing starts from 0 , We are going to take as 2:5")
print(b[2:5])

print("To slice from beginning , we use the syntax [:x] \n Example: To get from beginning to 5 letters . ie. 0 to 4th index :::  Hello \n we used to give [:5]")
print(b[:5])

print("Slice to end , we use the syntax [x:] \n Example: To get from the 5th index till end.\n  ie.from ",b," we used to give [5:] \n it starts from 0 and the 5th index is , till the end ")
print(b[5:])

print("Negative Indexing")
print("Negative Indexing to start the slice from the end of the string")
print(b[-5:-2])


# Variables and its data structures
#python have 4 types of built in Data Structures namely List, Dictionary, Tuple and Set.
myNumber = 3
print(myNumber)

myNumber = 4.5
print(myNumber)

myNumber = "Hello Beautiful!!!"
print(myNumber)

""" - MULTILINE COMMENT
List is the most basic Data Structure in python. List is a mutable data structure i.e items can be added to list later after the list creation.
 It's like you are going to shop at the local market and made a list of some items and later on you can add more and more items to the list.
append() function is used to add data to the list."""

#we are creating empty list
nums = []

#appending data in a list
nums.append(21)
nums.append(21.9)
nums.append("Just a example of different datatypes in list")
print(nums)

#INPUT & OUTPUT
name = input("Hey RockStar , Please type in your name : ")
print("Welcome RockStar "+name) #the return type of input is always string
#So lets look into how to get input as int

num1 = int(input("Enter a number since I am casting to int giving a value other than int throws valueError ::: "))


num2 = int(input("Enter a number since I am casting to int giving a value other than int throws valueError ::: "))


letsmultiplynum1num2 = num1*num2
print("Here your productvalue BaBe", letsmultiplynum1num2)

#select the selection
num1 = int(input("Enter a number : "))
if(num1 > 12):
    print("Hey Rocky , The number is cool since it is getter than 12", num1)
elif(num1 < 10):
    print("Hey Rocky, Thats ok sometimes we assume the number is lesser than required", num1)
else:
    print("number is lesser", num1)


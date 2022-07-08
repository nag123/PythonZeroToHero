'''
An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

In the Gregorian calendar, three conditions are used to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.
Task
IF(Y%400) => LP ELIF Y%100 => NLP  ELIF Y%4 => LP ELSE NLP
2000/4 => TRUE , 2000/400 => TRUE , 2000/100 => TRUE(nOT A LEAP YEAR)
2400/4          ,2400/400 =>        , 2400/100 =>
1800/4  T            1800/100  F         1800/400 F   => NT

Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

Input Format

Read , the year to test.

Constraints


Output Format

The function must return a Boolean value (True/False). Output is handled by the provided code stub.

Sample Input 0

1990
Sample Output 0

False
Explanation 0

1990 is not a multiple of 4 hence it's not a leap year.
IF(Y%400) => LP ELIF Y%100 => NLP  ELIF Y%4 => LP ELSE NLP
'''
def is_leap(year):
    leap = False
    if(year % 400 == 0): leap = True
    elif(year % 100 == 0): leap
    elif(year % 4 == 0): leap = True
    else : leap
    return leap


year = int(input("Enter the year to find its a leap year or not ::: "))
print(is_leap(year))
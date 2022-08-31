'''
    Point = namedtuple('Point', 'x,y')
    pt1 = Point(1,2)
    pt2 = Point(3,4)
    dot_product = (pt1.x * pt2.x) + (pt1.y * pt2.y)

    Car = namedtuple('Carsofcar', 'Price Mileage Colour Class')
    xyz = Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')

TASK:
Note:
1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)


TC-01
5
ID         MARKS      NAME       CLASS
1          97         Raymond    7
2          50         Steven     4
3          91         Adrian     9
4          72         Stewart    5
5          80         Peter      6

output: 78.00

TC - 02
5
MARKS      CLASS      NAME       ID
92         2          Calum      1
82         5          Scott      2
94         2          Jason      3
55         8          Glenn      4
82         2          Fergus     5

OUTPUT : 81.00

Explanation

TESTCASE 01

Average = (97+50+91+72+80)/5

Can you solve this challenge in 4 lines of code or less?
NOTE: There is no penalty for solutions that are correct but have more than 4 lines.
'''
from collections import namedtuple
if __name__ == "__main__":
    N = int(input())
    Student = namedtuple('Student123', input().split())
    sum = 0
    for i in range(N):
       sum+= int(Student(*input().split()).MARKS)
    print("{:.2f}".format(sum/N))


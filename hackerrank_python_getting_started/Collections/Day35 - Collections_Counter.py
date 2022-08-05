from collections import Counter
if __name__ == '__main__':
    #A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
    #myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3] #Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
    #print(Counter(myList))

    #print(Counter(myList).items()) #dict_items([(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)])
    #print(Counter(myList).keys()) #dict_keys([1, 2, 3, 4, 5])
    #print(Counter(myList).values()) #dict_values([3, 4, 4, 2, 1])

    '''
    Raghu is a shoe shop owner. His shop has  X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N  number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.

nput Format

The first line contains , the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains , the number of customers.
The next  lines contain the space separated values of the  desired by the customer and , the price of the shoe.
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
'''
    numberofshoes = int(input())
    allshoesintheshop = Counter(map(int,input().split()))
    noofcustomers = int(input())
    gainforraghu = 0
    for i in range(noofcustomers) :
        size , price = map(int,input().split())
        if(allshoesintheshop[size]):
            allshoesintheshop[size] -=1
            gainforraghu = gainforraghu + price
    print(gainforraghu)





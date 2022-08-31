'''
An OrderedDict is a dictionary that remembers the order of the keys that were inserted first.
If a new entry overwrites an existing entry, the original insertion position is left unchanged.

from collections import OrderedDict
if __name__ == "__main__":
    ordinary_dictionary = {}
    ordinary_dictionary['a'] = 1
    ordinary_dictionary['b'] = 2
    ordinary_dictionary['c'] = 3
    ordinary_dictionary['d'] = 4
    ordinary_dictionary['e'] = 5
    print(ordinary_dictionary)
    #The position/order is maintained
    ordered_dictionary = OrderedDict()
    ordered_dictionary['a'] = 1
    ordered_dictionary['b'] = 2
    ordered_dictionary['c'] = 3
    ordered_dictionary['d'] = 4
    ordered_dictionary['e'] = 5
    ordered_dictionary['e'] = 6

'''
from collections import OrderedDict
if __name__ == '__main__':
    n = int(input())
    ord_dict = OrderedDict()
    for i in range(n):
        items, price = input().rsplit(" ",1)
        ord_dict[items] = ord_dict.get(items,0) + int(price)
    for k,v in ord_dict.items():
        print(k,v)


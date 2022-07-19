'''
Task
Read a given string, change the character at a given index and then print the modified string.
Function Description

Complete the mutate_string function in the editor below.

mutate_string has the following parameters:

string string: the string to change
int position: the index to insert the character at
string character: the character to insert
Returns

string: the altered string
Input Format

The first line contains a string,String .
The next line contains an integer  position, the index location and a string character, separated by a space.

Sample Input
STDIN           Function
-----           --------
abracadabra     s = 'abracadabra'
5 k             position = 5, character = 'k'

output
abrackdabra
'''
def mutate_string(string, position, character):
    convertstringtolist = list(string)
    convertstringtolist[position] = character
    convertlistbacktostring = ''.join(convertstringtolist)
    return convertlistbacktostring

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    '''
       s = "abracadabra"
       print(s[5])
       l = list(s)
       l[5] = "k"
       res = "".join(l)
       print(res)
        '''
      #whenever we try to re-assign the value of a string s = "abracadabra" s[5] = 'k' we get error like
      #TypeError: 'str' object does not support item assignment
      #then how to change ?? Convert the string to list and then try to reassign because list are mutable whereas string is immutable
    

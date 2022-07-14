'''
Let's use decorators to build a name directory! You are given some information about  people. Each person has a first name, last name, age and sex. Print their names in a specific format sorted by their age in ascending order i.e. the youngest person's name should be printed first. For two people of the same age, print them in the order of their input.

For Henry Davids, the output should be:

Mr. Henry Davids
For Mary George, the output should be:

Ms. Mary George

Input Format

The first line contains the integer N , the number of people.
 lines follow each containing the space separated values of the first name, last name, age and sex, respectively.

Constraints
1<=N<=10

Output Format

Output  names on separate lines in the format described above in ascending order of age.


10
Jake Jake 42 M
Jake Kevin 57 M
Jake Michael 91 M
Kevin Jake 2 M
Kevin Kevin 44 M
Kevin Michael 100 M
Michael Jake 4 M
Michael Kevin 36 M
Michael Michael 15 M
Micheal Micheal 6 M

Expected Output
=====================
Mr. Kevin Jake
Mr. Michael Jake
Mr. Micheal Micheal
Mr. Michael Michael
Mr. Michael Kevin
Mr. Jake Jake
Mr. Kevin Kevin
Mr. Jake Kevin
Mr. Jake Michael
Mr. Kevin Michael
'''
import operator

def person_lister(f):
    def inner(people):
        # complete the function
        #return map(f,sorted(people,key=lambda x: x[2]))
        return map(f, sorted([[e[0], e[1], int(e[2]), e[3]] for e in people], key=operator.itemgetter(2)))
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print('\n'.join(name_format(people)))
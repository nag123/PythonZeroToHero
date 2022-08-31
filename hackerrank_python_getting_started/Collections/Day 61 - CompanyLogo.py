'''
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name.
 They are now trying out various combinations of company names and logos based on this condition.
 Given a string n, which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,

GOOGLE will have its logo's with letters - G,O,E

INPUT FORMAT :::
A single line of input containing the string .

Output Format

Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.

INPUT :
aabbbccde

OUTPUT :
b 3
a 2
c 2

Explanation 0

Here, b occurs 3 times. It is printed first.
Both a and c occur 2 times. So, a is printed in the second line and c in the third line
because a comes before c in the alphabet.

Note: The string S has at least  distinct 3 characters.

<<Pick only repeating letters and print the count of repeating letters>>
'''
from collections import Counter, OrderedDict

if __name__ == "__main__":

    for key, value in Counter(sorted(input())).most_common(3):
        print(f"{key} {value}", sep="\n")
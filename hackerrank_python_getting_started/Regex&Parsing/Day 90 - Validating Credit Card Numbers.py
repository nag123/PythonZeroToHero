'''
6
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456
'''
import re
if __name__ == "__main__":
    pattern_1 = re.compile(r'^(?=[4|5|6])(\d{4}\-?){3}\d{4}$')
    pattern_2 = re.compile(r'(\d)\1{3,}')

    n = int(input())
    cc_numb = []

    for _ in range(n):
        cc_numb.append(input())

    for cc in cc_numb:

        # check format
        if pattern_1.search(cc) == None:
            print("Invalid")
            continue

        # strip hyphens
        cc = cc.replace('-', '')

        # check repeats
        if pattern_2.search(cc) == None:
            print("Valid")
        else:
            print("Invalid")
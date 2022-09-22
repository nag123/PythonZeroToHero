# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import email.utils

if __name__ == "__main__":
    for i in range(int(input())):
        inputval = input()
        str = email.utils.parseaddr((inputval))
        value = str[1]
        reg = r"^[a-zA-Z][\w\-\.\_]+@[a-zA-Z]+[.][a-zA-Z]{1,3}$"
        match = re.search(reg, value)
        if match:
            print(inputval)



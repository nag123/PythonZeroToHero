import re

if __name__ == '__main__':
    userinput = int(input())

    for i in range(userinput):
        try:
            regexinput = re.compile(input())
            print(True)
        except re.error:
            print(False)



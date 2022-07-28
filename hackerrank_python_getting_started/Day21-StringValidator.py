# alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
def AlphaNum(s):
    result = False
    for character in range(len(s)):
        if (s[character].isalnum()): result = True
        else: pass
    return result

def AlphaLetters(s):
    result = False
    for character in range(len(s)):
        if (s[character].isalpha()):result = True
        else: pass
    return result

def Digit(s):
    result = False
    for character in range(len(s)):
        if (s[character].isdigit()): result = True
        else: pass
    return result


def UpperCase(s):
    result = False
    for character in range(len(s)):
        if (s[character].isupper()): result = True
        else: pass
    return result


def LowerCase(s):
    result = False
    for character in range(len(s)):
        if (s[character].islower()): result = True
        else: pass
    return result

if __name__ == '__main__':
    s = input()
    print(AlphaNum(s))
    print(AlphaLetters(s))
    print(Digit(s))
    print(LowerCase(s))
    print(UpperCase(s))

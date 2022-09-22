import re

if __name__ == "__main__":

    '''
    # Squaring numbers
    def square(match):
        number = int(match.group(0))
        return str(number ** 2)


    print(re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9"))
    '''
    strings = list(input() for i in range(int(input())))
    for i in strings:
        print(re.sub(r'(?<=\s)(\|\|)(?=\s)', r"or", re.sub(r'(?<=\s)(&&)(?=\s)', r"and", i)))
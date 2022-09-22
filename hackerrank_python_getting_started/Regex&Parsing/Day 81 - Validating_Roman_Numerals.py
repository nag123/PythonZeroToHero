import re
if __name__ == "__main__":
    regex_pattern = r""	# Do not delete 'r'.
    #print(str(bool(re.match(regex_pattern, input()))))
    # The number will be between 1 and 3999 (both included).

    # 1000 - 3000
    thousand = "M{0,3}"

    # 100 - 900
    # 100-300 | 400 | 500-800 | 900
    # C{0, 3}|CD|DC{0,3}|CM
    hundred = "(D?C{0,3}|C[DM])"
    # 10 - 90, 10-30 | 40 | 50-80 | 90
    ten = "(L?X{0,3}|X[LC])"
    # 1 - 9, 1-3, 4, 5-8, 9
    digit = "(V?I{0,3}|I[VX])"
    regex_pattern = r"%s%s%s%s$" % (thousand, hundred, ten, digit)  # Do not delete 'r'.
    print(str(bool(re.match(regex_pattern, input()))))
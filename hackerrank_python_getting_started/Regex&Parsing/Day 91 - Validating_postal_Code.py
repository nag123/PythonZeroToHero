if __name__ == "__main__":
    # P must be a number in the range from 100000  to 999999  inclusive.
    #so first digit (^) is between 1 to 9 rest of the 5 digits(digits - \d) of length 5 (length of 5 - {5}) at the end ($) are from 0 to 9
    regex_integer_in_range = r"^[1-9]\d{5}$"	# Do not delete 'r'.
    # P must not contain more than one alternating repetitive digit pair.
    #Checkes if the digit (\d) matches any character(.) in 1st capturing group(\1)
    regex_alternating_repetitive_digit_pair = r"(?=(\d).\1)"	# Do not delete 'r'.


    import re
    P = input()

    print (bool(re.match(regex_integer_in_range, P)) and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
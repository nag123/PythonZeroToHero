import math
if __name__ == '__main__':
    ab = float(input())
    bc = float(input())

    #print(str(round(math.degrees(math.atan2(ab, bc)))) + '°')
    # -> Error observed : Your submission contains non ASCII characters,
    # we dont accept submissions with non ASCII characters for this challenge.
    #Rectification ::
    print(str(round(math.degrees(math.atan2(ab, bc)))) + chr(176), sep='')

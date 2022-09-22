import re

if __name__ == "__main__":

  for _ in range(int(input())):
    str = input()
    match = re.search(r'^[789]\d{9}$', str)
    # If-statement after search() tests if it succeeded
    # \d - digit 0 to 9 and ^ - starting $ - End and {} - No of character
    if match:
      print('YES')
    else:
      print('NO')
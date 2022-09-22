# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = input()
pattern = re.compile(r"(?<![AEIOU])([AEIOU]{2,})(?![AEIOU]).", re.I)
res = pattern.findall(s)
if res:
    print(*res, sep='\n')
else:
    print(-1)
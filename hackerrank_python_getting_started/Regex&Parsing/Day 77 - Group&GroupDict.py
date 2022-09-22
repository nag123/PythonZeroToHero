import re

if __name__ == "__main__":
	n = input()
	pattern = re.compile(r"([\dA-Za-z])(?=\1)")
	s = pattern.search(n)
	if s:
		print(s.group(1))
	else:
		print(-1)
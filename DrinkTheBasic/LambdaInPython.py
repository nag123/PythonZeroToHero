n = int(input("Enter the term ::: "))
result = list(map(lambda x : x ** 2,range(n)))
# lambda gets pass to print
print('\n'.join([str(r) for r in result]))
# Covert list of integers to a string

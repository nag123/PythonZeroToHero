'''
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

'''
if __name__ == '__main__':
    N = int(input())
    output = []
    for i in range(N):
        datain = input().split()
        if datain[0] == "print" : print(output)
        elif datain[0] == "insert" : output.insert(int(datain[1]),int(datain[2]))
        elif datain[0] == "remove" : output.remove(int(datain[1]))
        elif datain[0] == "pop" : output.pop()
        elif datain[0] == "append" : output.append(int(datain[1]))
        elif datain[0] == "sort" : output.sort()
        else : output.reverse()





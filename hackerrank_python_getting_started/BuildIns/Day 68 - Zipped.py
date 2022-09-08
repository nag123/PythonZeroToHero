'''
input :
5 3
89 90 78 93 80
90 91 85 88 86
91 92 83 89 90.5

output :
90.0
91.0
82.0
90.0
85.5

Explanation

Marks obtained by student 1: 89,90,91
Average marks of student 1:270/3 = 90.0

Marks obtained by student 2:90,91,92
Average marks of student 2:273/3 = 91.0

Marks obtained by student 3:78,85,83
Average marks of student 3:246/3 = 82.0

Marks obtained by student 4:93,88,89
Average marks of student 4:270/3 = 90.0

Marks obtained by student 5:80,86,90.5
Average marks of student 5:256.50/3 = 85.5


'''
if __name__ == "__main__":
    columns, rows = map(int,input().split())
    columnvalues = []*columns
    for i in range(rows) :
        l = list(map(float, input().split()))
        columnvalues.append(l)
    for i in zip(*columnvalues):
        print(sum(i) / rows)




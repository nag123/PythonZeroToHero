from numpy import size
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = input()
    query_scores = list(student_marks[query_name])
    print("{0:.2f}".format(sum(query_scores) / (len(query_scores))))
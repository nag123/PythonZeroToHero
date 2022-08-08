if __name__ == '__main__':
    NoInASet = int(input())
    AsetValues = set(map(int, input().split()))
    NoInOtherSet = int(input())
    for i in range(NoInOtherSet):
        (command, newSet) = (input().split()[0],set(map(int, input().split())))
        if command == "update":
            AsetValues.update(set(map(int, newSet)))
        elif command == "intersection_update":
            AsetValues.intersection_update(set(map(int, newSet)))
        elif command == "difference_update":
            AsetValues.difference_update(set(map(int, newSet)))
        elif command == "symmetric_difference_update":
            AsetValues.symmetric_difference_update(set(map(int, newSet)))
        else:
            AsetValues
    print(sum(AsetValues))


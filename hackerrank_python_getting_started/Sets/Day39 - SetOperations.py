if __name__ == '__main__':
    N = int(input())
    valls = set(map(int, input().split()))
    totalnoofoperations = int(input())
    for i in range(totalnoofoperations):
        choice =input().split()
        if choice[0]=="pop" :
            valls.pop()
        elif choice[0] == "remove":
            valls.remove(int(choice[1]))
        elif choice[0] == "discard":
            valls.discard(int(choice[1]))
        else:
            valls

    print(sum(valls))

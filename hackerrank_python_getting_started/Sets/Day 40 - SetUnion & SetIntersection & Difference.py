if __name__ == '__main__':
    AteamTotal = int(input())
    AteamValues = ([int(i) for i in input().split(' ')])
    BteamTotal = int(input())
    BteamValues = ([int(i) for i in input().split(' ')])
    AteamValuesasSet = set(AteamValues)
    BteamValuesasSet= set(BteamValues)
    #Set Union code
    # print(len(AteamValuesasSet.union(BteamValuesasSet)))
    #Set intersection code
    #print(len(AteamValuesasSet.intersection(BteamValuesasSet)))
    #setDifference code
    print(len(AteamValuesasSet.difference(BteamValuesasSet)))




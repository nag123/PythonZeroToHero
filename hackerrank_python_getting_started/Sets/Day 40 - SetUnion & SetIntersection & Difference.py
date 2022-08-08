if __name__ == '__main__':
    AteamTotal = int(input())
    AteamValues = ([int(i) for i in input().split(' ')])
    BteamTotal = int(input())
    BteamValues = ([int(i) for i in input().split(' ')])
    AteamValuesasSet = set(AteamValues)
    BteamValuesasSet= set(BteamValues)
    #print(len(AteamValuesasSet.union(BteamValuesasSet)))
    #print(len(AteamValuesasSet.intersection(BteamValuesasSet)))
    print(len(AteamValuesasSet.difference(BteamValuesasSet)))




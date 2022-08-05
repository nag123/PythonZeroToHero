if __name__ == '__main__':
    '''    s = set('HackerRank')
    s.add('H')
    print(s)
    It outputs {'r', 'k', 'H', 'c', 'R', 'e', 'n', 'a'}
     Why ? ::: Because set doesnt allow duplicate letters
    print(s.add('HackerRank'))
    print(s)
    '''
    stampcountfromrupal = int(input())
    countrystamps = set()
    for _ in range(stampcountfromrupal):
        countrystamps.add(input().strip())
    print(len(countrystamps))

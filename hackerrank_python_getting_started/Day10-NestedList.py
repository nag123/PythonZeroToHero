if __name__ == '__main__':
    scorelist = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scorelist.append([name,score])
    print(scorelist)
    SecondHighest= sorted(set([score for name, score in scorelist]))[1]
   # print(secondlowest)
   # print(sorted(set([score for name, score in scorelist]))[1])
    '''
    
print('\n'.join(sorted([name for name, score in score_list if score == second_highest])))
# Nested Lists in Python - Hacker Rank Solution END
'''
    print('\n'.join(sorted([name for name, score in scorelist if score == SecondHighest])))
'''
B
BA          A
BAN         AN      N
BANA        ANA     NA      A
BANAN       ANAN    NAN     AN      N
BANANA      ANANA   NANA    ANA     NA      A

6           5       4       3       2       1

6+4+2 = 12
5+3+1 = 9


'''
def minion_game(string):
    # your code goes here
    s = len(string)
    vowel = 0
    consonant = 0

    for i in range(s):
        if string[i] in 'AEIOU':
            vowel += (s - i) # 0+(6-1) ->5 #5+(6-3) -> 8
        else:
            consonant += (s - i) #0+(6-0)-> 6 #6+(6-2) ->10

    if(vowel > consonant):
        print("Kevin",vowel)
    elif(consonant > vowel):
        print("Stuart", consonant)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
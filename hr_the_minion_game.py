"""
# 100daysCodingChallenge
Level: Medium

Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, S
.
Both players have to make substrings using the letters of the string S

.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string S

Example:

String = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

"""
# This is my solution which is incomplete and timing out in hackerRank when given
# large numbers
# todo: Fix the timing out at Large numbers
import sys
def getSub_words(string, workDict, stringLen):
    # {'b': [0], 'n': [3, 5], 's': [7]}
    # {'a': [1, 2, 4, 6]}
    subs = []
    for key,sindex in workDict.items():
        for s in sindex:
            for i in range(s, stringLen+1):
                if string[s:i] != "":
                    if not string[s:i] in subs:
                        subs.append(string[s:i])

    print(subs)
    score = 0
    for word in subs:
        l = [n for n in range(len(string)) if string.find(word, n) == n]
        score += len(l)

    return score


def minion_game(string):
    # kevin = vowels
    # stuart = consonants
    if not string.isupper():
        sys.exit(1)

    if len(string) > 10**6 or len(string) < 0:
        sys.exit(1)

    string = string.lower()
    vowels = ["a", "e", "i", "o", "u"]
    mystring = [letter for i, letter in enumerate(string)]
    kevin_words = {}
    stuart_words = {}
    for l in mystring:
        if l in vowels:
            # if l not in kevin_words.items():
            kevin_words[l] = [n for n in range(len(string)+1) if string.find(l, n) == n]

        if l not in vowels:
            # if l not in stuart_words.items():
            stuart_words[l] = [n for n in range(len(string)+1) if string.find(l, n) == n]

    # print(kevin_words)
    # print(stuart_words)
    stuart_subs = []
    stringLen = len(string)
    # print(stuart_words)
    # print(kevin_words)
    stuart_score = getSub_words(string, stuart_words, stringLen)
    kevin_score = getSub_words(string, kevin_words, stringLen)
    #
    # if stuart_score > kevin_score:
    #     print("Stuart {}".format(stuart_score))
    # elif kevin_score > stuart_score:
    #     print("Kevin {}".format(kevin_score))
    # else:
    #     print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)

"""
# working code

def minion_game1(s):
    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s)-i)
        else:
            stusc += (len(s)-i)

    if kevsc > stusc:
        print("Kevin {}".format(kevsc))
    elif kevsc < stusc:
        print("Stuart {} ".format(stusc))
    else:
        print("Draw")
"""

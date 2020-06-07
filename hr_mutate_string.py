"""
# 100daysCodingChallenge - Day 3
Level: Easy

"""

def mutate_string(string, position, character):
    split_string = list(string)
    split_string[position] = character
    join_string = "".join(split_string)

    return join_string


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

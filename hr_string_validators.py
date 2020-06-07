"""
# 100daysCodingChallenge
Level: Easy

You are given a string S
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format:
    A single line containing a string S

Output:
    In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
In the second line, print True if S has any alphabetical characters. Otherwise, print False.
In the third line, print True if  S has any digits. Otherwise, print False.
In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
In the fifth line, print True if S has any uppercase characters. Otherwise, print False.

Sample Input:

qA2

Sample Output:

True
True
True
True
True
"""
import sys
if __name__ == '__main__':
    s = input()
    newlist = list(s)

    slen = len(s)
    if slen > 1000 or slen < 0:
        sys.exit(1)
    upper = False
    lower = False
    alpha = False
    alphaNum = False
    digit = False

    for s in newlist:
        if s.isupper():
            upper = True
        if s.islower():
            lower = True
        if s.isalpha():
            alpha = True
        if s.isalnum():
            alphaNum = True
        if s.isdigit():
            digit = True

print(alphaNum)
print(alpha)
print(digit)
print(lower)
print(upper)

"""
Learnings:
    Just different types of String validation functions 
"""

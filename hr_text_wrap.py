"""
# 100daysCodingChallenge
Level: Easy

You are given a string S and width W, make a word wrap at given length

"""

import textwrap
import sys

def wrap(string, max_width):
    sLen = len(string)
    if sLen > 1000 or sLen < 0:
        sys.exit(1)

    if max_width > sLen or max_width  < 0:
        sys.exit(1)

    wrapper = textwrap.TextWrapper(width=max_width)
    word_list = wrapper.wrap(text=string)
    word_list = "\n".join(word_list)
    return word_list

if __name__ == '__main__':
    string, max_width = input(), int(input())
    word_list = wrap(string, max_width)
    print(word_list)

"""
Learnings:
    Use of textwrap library to break string at particular length
"""

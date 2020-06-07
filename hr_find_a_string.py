"""
# 100daysCodingChallenge
Level: Easy

In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string.
 String traversal will take place from left to right, not from right to left.

Note: Strings are Case Sensitive

Constraints:
    1 <= len(string) <= 200

Ouptut Format:
    Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input:
    ABCDCDC
    CDC

ouptut:
    2

"""
import sys
def count_substring(string, sub_string):
    str_len = len(string)
    if str_len > 200 or str_len < 1:
        sys.exit(1)
    count = 0
    t = sub_string[0]
    # using enumerate I am checking index position of the all matching characters in the given string and creating a list of it
    occurences = [i for i, letter in enumerate(string) if letter == t]
    subLen = len(sub_string)
    for o in occurences:
        val = string.find(sub_string, o, o+subLen)
        if int(val) >= 0:
            count += 1

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)

"""
Learnings:
    Enumerate function: Using of enumerate function to iterate over a string and figure out number of
    occurrences of that character

    string.find() function: Find the occurrence of a substing at particular location else it will return -1
    string.find(sub_string, start_index, end_index) --> will look for a substring between this indexes
"""

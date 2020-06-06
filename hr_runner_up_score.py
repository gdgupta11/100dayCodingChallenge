"""
# 100daysCodingChallenge
Level: Easy

Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
 You are given scores. Store them in a list and find the score of the runner-up.

 Input Format:

 The first line contains n . The second line contains an array A[] of n integers each separated by a space.

 Output Format:

 Print the runner up score
"""
import sys
if __name__ == "__main__":
    n = int(input())
    if n > 10 or n < 2:
        sys.exit(1)
    # converting the map into list to make it more usable
    arr = list(map(int, input().split()))
    if len(arr) != n:
        sys.exit(1)
    arr.sort()
    # creating a set to get unqiue values, then again converting it to get back the second lowest value using reverse indexing in lists
    tmpList = list(set(arr))
    tmpList.sort()
    # sorting again to check the usecase where integers are mix of negative and postive numbers
    tmpList = tmpList[-2]
    print(tmpList)

"""
Learnings:

Using of Map function to get input and then converting it into list

Edge cases covered:
    1. Checking if input n (integer) is between 10 and 2
    2. Exiting on non-negative numbers
    3. Exiting if number of integers input does not match len of integers
"""

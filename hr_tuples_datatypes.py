"""
# 100daysCodingChallenge
Level: Easy
Task:

Given an integer n and n space separated integers as input, create a tuple, t of those integers. Then compute and print the result of hash(t)

Hint: hash() is the inbuilt function in the python

Output: Print the result of hash(t)



"""
import sys
if __name__ == '__main__':
    # the input should be non negative integer. Converting that into abs value
    n = abs(int(input()))
    # this takes the list which has integer inputs and convert them all into int
    integer_list = list(map(int, input().split()))
    mylist = list(integer_list)
    # exiting if the n spaced integers isn't equal to integer n
    if len(mylist) != n:
        sys.exit(1)
    print(hash(tuple(mylist)))

"""
Learnings from this:

1.Use of hash function to create hash() of any given object

2. Use of map function to take input and split that by spaces. That creates map object
Converting that map object into list and tuple for creating hash of it.
"""

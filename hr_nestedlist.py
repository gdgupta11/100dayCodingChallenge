"""
# 100daysCodingChallenge

Given the names and grades for each student in a Physics class of

students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer,
, the number of students.
The subsequent lines describe each student over

lines; the first line contains a student's name, and the second line contains their grade.

Constraints: 2 <= N <= 5

There will always be one or more students having the second lowest grade.

Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.
"""

if __name__ == "__main__":
    main_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        main_list.append([name, score])

    main_list.sort(key = lambda main_list: main_list[1])
    tmpList = [lst[1] for lst in main_list]
    tmpList = set(tmpList)

    name_list = []
    testList = []
    for l in tmpList:
        testList.append(l)
    testList.sort()
    for lst in main_list:
        if lst[1] == testList[1]:
            name_list.append(lst[0])

    name_list.sort()
    for name in name_list:
        print(name)

"""
# 100daysCodingChallenge - Day 3
Level: Easy

You have a record of N students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry.
The marks can be floating values. The user enters some integer followed by the names and marks for students.
You are required to save the record in a dictionary data type.
 The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.

 Constraints:
2 <= N  <= 10
0 <= Marks <= 100

Sample Input:

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output:

56.00
"""
import sys
if __name__ == "__main__":
    n = int(input())
    # validating if input is between 2 and 10
    if n > 10 or n < 2:
        sys.exit(1)

    student_marks = {}
    for _ in range(n):
        # splitting the line Krishna 67 68 69 in name and list of numbers
        name, *line = input().split()
        # converting those scores into floating numbers using map
        scores = list(map(float, line))
        # Validating is scores are between 0 and 100
        for s in scores:
            if s > 100 or s < 0:
                sys.exit()
        student_marks[name] = scores
    query_name = input()

    # taking out average:
    new_dict = {}
    # print(student_marks)
    for name,scores in student_marks.items():
        total = 0
        length = len(scores)
        for v in scores:
            total += v
            percentage = float(total/length)
        new_dict[name] = [scores, percentage]

    # print("The final dict with percentage is: {} ".format(new_dict))
    if query_name in new_dict.keys():
        print("{:.2f}".format(new_dict[query_name][1]))

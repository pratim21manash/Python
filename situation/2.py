# QUESTION 2: Student Marks Analyzer
#     📌 Problem Statement (only the question)
#     You are given a list of marks scored by students.
#     You need to:
#     Calculate the average marks
#     Count how many students passed (marks ≥ 40)
#     Find the highest mark

marks = [85, 42, 39, 76, 90, 28, 55, 67, 45, 33]

total_marks = 0
passed_students = 0
highest_mark = marks[0]

for mark in marks:
    total_marks = total_marks + mark

    if mark >= 40:
        passed_students = passed_students + 1
    
    if mark > highest_mark:
        highest_mark = mark

average = total_marks / len(marks)
print("Average Marks:", average)
print("Passed Students:", passed_students)
print("Highest Mark:", highest_mark)
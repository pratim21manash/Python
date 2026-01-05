# 1. Daily Expense Tracker
#     You are given a list of daily expenses.
#     Calculate total expense
#     Find highest expense
#     Count days above ₹500

expenses = [450, 600, 750, 300, 500, 900, 200]

#calculate total expense
total_expense = 0
for expense in expenses:
    total_expense += expense
print("Total Expense: ₹", total_expense)

#Find highest expense
highest_expense = expenses[0]

for amount in expenses:
    if amount > highest_expense:
        highest_expense = amount
print("Highest Expense: ₹", highest_expense)


#Count days above ₹500
count_above_500 = 0
for amount in expenses:
    if amount > 500:
        count_above_500 += 1
print("Days with expense above ₹500:", count_above_500)
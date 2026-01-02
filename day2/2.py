expenses = [200, 150, 300, 250, 180]

# expenses over 200rs
for expense in expenses:
    if expense > 200:
        print("Expense over 200 rs is", expense)

# Total monthly expense
total = 0
for expense in expenses:
    total += expense
print("Total monthly expense is:", total)


# Highest expense
highest = expenses[0]
for expense in expenses:
    if expense > highest:
        highest = expense
        print("Highest expense so far is:", highest)


# Lowest expense
lowest = expenses[0]

for expense in expenses:
    if expense < lowest:
        lowest = expense
        print("Lowest expense so far is:", lowest)

# Average daily expense
total = 0
for expense in expenses:
    total += expense
    
    average = total / len(expenses)
    print("Average daily expense is:", average)
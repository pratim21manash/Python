# Create a list of daily expenses for 5 days and print all expenses.

expenses = [200, 150, 300, 100, 250]

for expense in expenses:
    print("Expense:", expenses)


# 2️⃣ First & Last Expense
# From the expense list, print the first and last expense.
print("First Expense:", expenses[0])
print("Last Expenses", expenses[-1])

# 3️⃣ Update an Expense
expenses[2] = 700
print("Updated Expenses is:", expenses)

# Count Days
print("Total number of days with expenses record is:", len(expenses))

# Add new expenses
expenses.append(400)
print(expenses)
# 1️⃣1️⃣ Attendance Tracker

# attendance = ["P", "A", "P", "P", "A", "P", "P"]

# present_count = 0
# absent_count = 0

# for day in attendance:
#     if day == "P":
#         present_count += 1
#     elif day == "A":
#         absent_count += 1

# print("Total present days:", present_count)
# print("Total absent days:", absent_count)



# Search list

expenses = [200, 150, 300, 250, 180]

value = 300

if value in expenses:
    print("Found")
else:
    print("Not Found")


# Remove wrong entry
expenses.remove(150)
print(expenses)


# Duplicate expenses
has_duplicate = false

for expense in expenses:
    if expenses.count(expense) > 1:
        has_duplicate = True

print(has_duplicate)
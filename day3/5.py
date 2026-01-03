# Print multiplication table of a number

# num = int(input("Enter number: "))

# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)


# Find the sum of numbers from 1 to n
# n = int(input("Enter a number: "))
# total = 0

# for i in range(1, n + 1):
#     total += i

# print("Sum from 1 to", n, "is", total)



#count numbers disvisuble by 3 and 5 betwee 1 to n

count = 0

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        count += 1

print("Count of numbers divisible by 3 and 5 betwee 1 to 100 is:", count)
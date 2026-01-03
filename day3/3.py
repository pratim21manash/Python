# Count how many numbers are divisible by 3 (1–50)

count = 0

for i in range(1, 51):
    if i % 3 == 0:
        count += 1

print("Count of numbers divisible by 3 from 1 to 50:", count)
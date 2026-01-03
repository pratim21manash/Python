# 🧠 PROBLEM STATEMENT (Human Language)

# Build a simple ATM system that:

# • Shows a menu repeatedly
# • Allows the user to
# 1️⃣ Check Balance
# 2️⃣ Deposit Money
# 3️⃣ Withdraw Money
# 4️⃣ Exit

# • Updates balance correctly
# • Stops only when the user chooses Exit

# This is exactly how an ATM works.

# 🧩 RULES (IMPORTANT)

# Start with an initial balance (example: ₹10,000)

# User can perform multiple operations

# Withdrawal not allowed if balance is insufficient

# Program must keep running until Exit is chosen



balance = 10000

while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Your balance is:", balance)

    elif choice == "2":
        amount = int(input("Enter deposit amount: "))
        balance += amount
        print("Deposit successful")

    elif choice == "3":
        amount = int(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print("Please collect your cash")
        else:
            print("Insufficient balance")

    elif choice == "4":
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice, try again")

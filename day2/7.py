# Login validation system

correct_username = "admin"
correct_password = "12345"

username = input("Enter usename: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Logn successful")
else:
    print("Invalid credintials")
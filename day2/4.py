# Question 1: User Profile (Dictionary)

# Problem
# Store a user’s name, age, city in a dictionary and print all values.

# user = {
#     "name": "Manash",
#     "age": 23,
#     "city": "Guwahati"
# }

# print(user["name"])
# print(user["age"])
# print(user["city"])

# for key in user:
#     print(user[key])



# Question 2: Product Info (Dictionary)

# Problem
# Create a dictionary for a product with name, price, stock.
# product = {
#     "name": "Laptop",
#     "price": 50000,
#     "stock": 10
# }

# print(product["name"])
# print(product["price"])
# print(product["stock"])



products = [
    {
        "name": "Laptop",
        "price": 50000,
        "stock": 10
    }
]

for product in products:
    for key in product:
        print(product[key])
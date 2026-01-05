# 🧠 QUESTION 3: Grocery Bill Calculator
#     You are given grocery items, where each item has:
#     a price
#     a quantity
#     You need to:
#     Calculate the total grocery bill
#     Find the most expensive item (by price)

groceries = [
    {"name": "Rice", "price": 60, "qty": 2},
    {"name": "Milk", "price": 50, "qty": 3},
    {"name": "Oil", "price": 180, "qty": 1},
    {"name": "Sugar", "price": 45, "qty": 2}
]

total_bill = 0
total_items = 0
most_expensive_price = groceries[0]["price"]
most_expensive_item = groceries[0]["name"]

for item in groceries:
    item_total = item["price"] * item["qty"]
    total_bill = total_bill + item_total

    
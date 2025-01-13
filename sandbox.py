sandwich_orders = [
    "Pastrami",
    "Turkey Sandwich",
    "Ham and Cheese Sandwich",
    "Chicken Salad Sandwich",
    "Egg Salad Sandwich",
    "Pastrami",
    "Pastrami",
    "Peanut Butter and Jelly Sandwich",
]
lower_case = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    lower_case.append(sandwich.lower())

print(sandwich_orders)
print(lower_case)
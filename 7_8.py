sandwich_orders = [
    "Turkey Sandwich",
    "Ham and Cheese Sandwich",
    "Chicken Salad Sandwich",
    "Egg Salad Sandwich",
    "Peanut Butter and Jelly Sandwich",
]

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich}")

    finished_sandwiches.append(current_sandwich)

for sandwich in finished_sandwiches:
    print(f"{sandwich} is made")

pizzas = ["hawaiian", "pepperoni", "supreme"]

friend_pizzas = pizzas[:]

pizzas.append("ham and cheese")
friend_pizzas.append("four cheese")

print("My favorite pizzas are")
for pizza in pizzas:
    print(pizza)

print("My friend’s favorite pizzas are")
for pizza in friend_pizzas:
    print(pizza)

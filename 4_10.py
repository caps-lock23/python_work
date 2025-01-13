foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
print("The first three items in the list are:")
for food in foods[:3]:
    print(food)
print("Three items from the middle of the list are:")
for food in foods[1:4]:
    print(food)
print("The last three items in the list are:")
for food in foods[-3:]:
    print(food)
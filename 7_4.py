active = True

while active:
    topping = input("Enter a pizza topping: ")
    if topping != 'quit':
        print(f"I'll add {topping} to your pizza")
    elif topping == 'quit':
        break
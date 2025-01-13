active = True

while active:
    age = int(input("What is your age? "))
    
    if age < 0:
        break
    elif age < 3:
        print("The ticket is free")
    elif age >= 3 and age <= 12:
        print("The ticket is $10")
    elif age > 12:
        print("The ticket is $15")
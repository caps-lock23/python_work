count = input("How many people are in their dinner group? ")
count = int(count)
if count > 8:
    print("You will have to wait for a table")
elif count <= 8:
    print("Your table is ready")

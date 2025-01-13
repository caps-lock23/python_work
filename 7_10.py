responses = {}

polling_active = True

while polling_active:
    name = input("What is your name? ")
    response = input("Where is your dream vacation? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no) ").lower()
    if repeat == 'no':
        polling_active = False

print("\n--- Polling Results ---")
for name, response in responses.items():
    print(f"{name} would like to go to {response}")
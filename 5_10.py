current_username = ["admin", "grd", "go", "cada", "g23"]
new_username = ["ADMIN", "drg", "adac", "goc", "g23"]

for item in new_username:
    if item.lower() in current_username:
        print("Enter a new username")
    else:
        print("Username is available")
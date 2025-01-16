from pathlib import Path
import json

def get_stored_number(path):
    if path.exists():
        content = path.read_text()
        favorite_number = json.loads(content)
        return favorite_number
    else:
        return

def get_new_number(path):
    favorite_number = input('What is your favorite number? ')
    contents = json.dumps(favorite_number)
    path.write_text(contents)
    return favorite_number


def fav_num():
    """Get favorite number"""
    path = Path('favorite.py')
    favorite_number = get_stored_number(path)
    if favorite_number:
        print(f"I know your favorite number! It's : {favorite_number}")
    else:
        get_new_number(path)
        print("We'll remember your number when your back")

fav_num()


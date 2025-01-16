from pathlib import Path
import json

def get_stored_info(path):
    """Get stored info if available."""
    if path.exists():
        contents = path.read_text()
        info = json.loads(contents)
        return info
    else:
        return None

def get_new_info(path):
    """Prompt for new info."""
    info = {}
    username = input("What is your name? ")
    nationality = input("What is your nationality? ")
    color = input("What is your favorite color? ")

    info["name"] = username
    info["nationality"] = nationality
    info["color"] = color

    contents = json.dumps(info)
    path.write_text(contents)
    return info

def prompt_user():
    """prompt user"""
    path = Path('info.json')
    info = get_stored_info(path)
    if info:
        print(f"Welcome back, {info["name"]}!\nYour nationality is {info["nationality"]}\nYour favorite color is {info["color"]}")
    else:
        info = get_new_info(path)
        print(f"We'll remember you when you come back, {info["name"]}!")

prompt_user()
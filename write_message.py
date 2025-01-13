from pathlib import Path

contents = "I love programing.\n"
contents += "I love creating games.\n"
contents += "I also love working with data.\n"

path = Path('programming.txt')
path.write_text(contents)
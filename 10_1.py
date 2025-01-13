from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

print(contents)

lines = contents.splitlines()
read_string = ''
for line in lines:
    line += " "
    read_string += line

print(read_string)

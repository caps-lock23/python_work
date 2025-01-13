from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

contents = contents.replace('Python', 'C')

print(contents)

read_string = ''
for line in contents.splitlines():
    line += " "
    read_string += line

read_string = read_string.replace('Python', 'C')

print(read_string)
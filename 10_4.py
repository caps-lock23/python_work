from pathlib import Path

path = Path('guest.txt')

fullname = input('Input your fullname: ')

path.write_text(fullname)
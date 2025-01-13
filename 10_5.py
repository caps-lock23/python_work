from pathlib import Path

path = Path('guest_book.txt')

print('enter \'q\' to quit anytime')
name = ''

while True:
    user_input = input('Enter your fullname: ')
    if user_input.lower() == 'q':
        break
    name += user_input + '\n'


path.write_text(name)
print("Guest book saved!")
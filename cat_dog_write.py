from pathlib import Path

def write(path):
    text = ''
    while True:
        name = input('Enter names: ') 
        if name.lower() == 'q':
            break
        text += name +'\n'
    
    path.write_text(text)

cats = Path('cats.txt')
dogs = Path('dogs.txt')

print('Enter your cat names: ')
write(cats)
print('Enter your dog names: ')
write(dogs)


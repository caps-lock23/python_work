from pathlib import Path

def show_text(path):
    try:
        text = path.read_text()
    except FileNotFoundError:
        print(f'{path} is missing')
    else:
        print(text)


filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    path = Path(filename)
    show_text(path)


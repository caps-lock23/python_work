from pathlib import Path

def show_text(path):
    try:
        text = path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(text)


filenames = ['cats.txt', 'dog.txt']
for filename in filenames:
    path = Path(filename)
    show_text(path)


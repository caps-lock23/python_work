from pathlib import Path

def word_count(path):
    try:
        book = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        print(book.lower().count('the'))

books = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for book in books:
    path = Path(book)
    word_count(path)

def make_album(artist, title, number = None):
    if number:
        album = {'artist': artist, 'title': title, 'number': number}
    else:
        album = {'artist': artist, 'title': title}

    return album

while True:
    print("Enter the following values ")
    print("(enter 'q' at any time to quit)")

    artist = input("Artist: ")
    if artist == 'q':
        break

    title = input("Title: ")
    if artist == 'q':
        break

    album = make_album(artist, title)
    print(album)

# album1 = make_album('Pink Floyd', 'The Dark Side of the Moon')
# album2 = make_album('The Beatles', 'Abbey Road', 6)
# album3 = make_album('Taylor Swift', '1989')

# print(album1)
# print(album2)
# print(album3)
# print(album1['artist'])
# print(album1['title'])
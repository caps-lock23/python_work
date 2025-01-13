glossary = {'first' : 'first definition', 'second' : 'second definition', 'third' : 'third definition'}
glossary['fourth'] = 'fourth definition'
glossary['fifth'] = 'fifth definition'

for word, definition in glossary.items():
    print(f"{word} : {definition}")
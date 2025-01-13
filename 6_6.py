favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

friends = ['jen', 'sarah', 'bill', 'gary']

for name in friends:
    if name in favorite_languages.keys():
        print(f'Thank you {name.title()} for taking the poll')
    elif name not in favorite_languages.keys():
        print(f'{name.title()}, you should take the poll')
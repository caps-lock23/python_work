from random import choices

list = ['a', 'b', 'c', 'd', 'e', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

win = choices(list, k = 4)

print(f'Winners have {win} in their ticket')


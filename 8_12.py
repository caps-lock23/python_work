def sandwich_maker(*item):
    print("You put this/these in your sandwich:")
    for i in item:
        print(i)

sandwich_maker('ham')
print('\n')
sandwich_maker('ham', 'cheese', 'egg')


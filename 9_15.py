from random import choices

list = ['a', 'b', 'c', 'd', 'e', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

win = choices(list, k = 4)

my_ticket = ['a', 'b', 'c', 3]

lose = True
count = 0

while lose:  
    if set(my_ticket) == set(win):
        lose = False
        print(f"you won the lottery within {count} times")
    else:
        win = choices(list, k = 4)
        print(win)
        count += 1


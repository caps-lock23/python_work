# sentence = "This is a sentence, get the longest word and count how many words in it"

# sentence= sentence.split()
# max_len = 0
# longest_word = ''

# for item in sentence:
#     if len(item) > max_len:
#         max_len = len(item)
#         longest_word = item

# print(f'The longest word is {longest_word}\nIt has {max_len} word count')

array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

array[1].reverse()

for i in range(len(array)):
    for j in range(len(array[i])):
        print(f"{array[i][j]} ", end="")
    print()

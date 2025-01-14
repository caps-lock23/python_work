sentence = "This is a sentence, get the longest word and count how many words in it"

sentence= sentence.split()
max_len = 0
longest_word = ''

for item in sentence:
    if len(item) > max_len:
        max_len = len(item)
        longest_word = item

print(f'The longest word is {longest_word}\nIt has {max_len} word count')
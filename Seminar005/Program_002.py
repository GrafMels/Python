from encodings import utf_8

path = 'File_002.txt'

data_strings = ''

with open(path, 'r', encoding='utf_8') as data:
    data_strings = data.read()



find_txt = 'абв'

data_strings = data_strings.split()


result_txt = []

for word in data_strings:
    if find_txt not in word:
        result_txt.append(word)

print(result_txt)

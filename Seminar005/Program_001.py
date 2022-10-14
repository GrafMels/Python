from random import randint

len_list_1 = randint(5, 10)

list_1 = [i for i in range(len_list_1)]

print(list_1)

list_1.pop(randint(1, len_list_1-2))

with open('File_001.txt', 'w') as data:
    for i in range(len_list_1-1):
        data.write(f'{i} ')
        if list_1[i] - 1 != list_1[i-1] and i != 0:
            print(i)

print(list_1)

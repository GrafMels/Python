import random

amount_list = int(input('Введите колличество элементов в списке, а я выдам рандомный список: '))

list = []
number_of_characters = 6 # колличество знаков после запятой в ответе, для того что бы выглядел красиво

for i in range(amount_list):
    list.append(round(random.uniform(-10, 10), number_of_characters))

print(list)

for i in range(amount_list):
    list[i] = list[i]%1

index_of_zeros = []
counter = 0

while min(list) == 0:
    index_of_zeros.append(list.index(min(list)))
    list.pop(index_of_zeros[counter])
    counter += 1
# Берём нулевые значения и временно их удаляем

answer = [max(list), min(list)]
answer.append(answer[0]-answer[1])
# Считаем максимальное - минимально

if counter > 0:
    for i in range(counter):
       list.insert(0, index_of_zeros[i])
# Возвращаем на место нули(¯\_(ツ)_/¯, просто что бы показать что можно сохранить список)

print(f'{round(answer[0], 6)} - {round(answer[1], 6)} = {round(answer[2], 6)}')


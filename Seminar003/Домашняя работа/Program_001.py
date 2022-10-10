import random

amount_list = int(input('Введите колличество элементов в списке, а я выдам рандомный список и посчитаю сумму элементов на  нечётных индексах: '))

list = []

for i in range(amount_list):
    list.append(random.randint(-10, 10))

print(list)

sum_odd_numer = 0

for i in range(1, amount_list, 2):
    sum_odd_numer += list[i]

print(sum_odd_numer) 
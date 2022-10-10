import random
import math

amount_list = int(input('Введите колличество элементов в списке, а я выдам рандомный список: '))

list = []

for i in range(amount_list):
    list.append(random.randint(-10, 10))

print(list)

couples_list = []

for i in range(math.ceil((amount_list/2))):
    couples_list.append(list[i]*list[-(i+1)])

print(couples_list) 
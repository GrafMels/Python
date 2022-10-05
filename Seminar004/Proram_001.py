# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.
from random import randint

N = int(input('Введите число: '))
list = []

for i in range(N):
    list.append(randint(-99, 99))


with open('file.txt', 'w') as data:
    data.write(f"{str(list[i-1])}")
    for i in range(1,N):
        data.write(f" {str(list[i-1])}")
    data.close()



with open("file.txt") as file:
    for line in file:
        data = ([int(x) for x in line.split()])

min = min(data)
max = max(data)

with open('MyFile.txt', 'w') as data:
    
    data.write(f'Max = {max}\n')
    data.write(f'Min = {min}')
    data.close()
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

import math

N = float(input('Введите число: '))


len_N = len(str(N))

N_larger_one = int(N//1)
len_N_larger_one = len(str(N_larger_one))

N_smaller_one = int((N-N_larger_one)*(10**(len_N-len_N_larger_one-1)))
len_N_smaller_one = len(str(N_smaller_one))

count = 1
list = []

list.append(N_smaller_one % (10))
count += 1

for i in range(1, len_N_smaller_one):
    list.append(int((N_smaller_one % (10 ** (i + 1)) - N_smaller_one % (10 ** i))// 10 ** i))
    print(list)
    count += 1
    if (len_N_larger_one == i): break

list.append(len_N_smaller_one % (10))


for i in range(1, len_N_larger_one):
    list.append(int((N_larger_one % (10 ** (i + 1)) - N_larger_one % (10 ** i))// 10 ** i))
    print(list)
    count += 1
    if (len_N_larger_one == i): break

sum = 0

for i in range(count):
    sum += list[i]


print(sum)


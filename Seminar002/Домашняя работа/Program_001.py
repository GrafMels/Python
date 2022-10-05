# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

import math

N = input('Введите вещественное число: ')

if '.' in N:
    divided = N.split(".")
    len_N = len(N)
else:
    divided = [N, 0]
    len_N = len(N)

count = 0
list = []


def Add_In_List(divided, list, count):

    N_some_one = int(divided)
    len_N_some_one = len(divided)

    list.append(N_some_one % (10))
    count += 1

    for i in range(1, len_N_some_one):
        list.append(int((N_some_one % (10 ** (i + 1)) -
                    N_some_one % (10 ** i)) // 10 ** i))
        count += 1
        if (len_N_some_one == i):
            break

    return list, count


if divided[1] == 0:

    list, count = Add_In_List(divided[0], list, count)

elif divided[0] == 0:

    list, count = Add_In_List(divided[1], list, count)

else:
    list, count = Add_In_List(divided[1], list, count)
    list, count = Add_In_List(divided[0], list, count)

sum = 0

for i in range(count):
    sum += list[i]


print(sum)

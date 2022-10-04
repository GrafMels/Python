# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Пример:
# o Для N = 5: 1, -3, 9, -27, 81
N=int(input('Введите число N: '))

def posled(N):
    array = []

    # num = 1
    for i in range(N):
        array.append((-3) ** i)
        # num *= -3
    return array

array = posled(N)
print(array)


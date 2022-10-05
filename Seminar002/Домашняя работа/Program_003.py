# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

N = int(input('Введите число: '))

list = []
fun = 1

for i in range(2, N+2):
    for j in range(1, i):
        fun = (1 +(1 / fun)) ** fun
    print(round(fun, 2))
    list.append(round(fun, 2))
    fun = 1
print(round(sum(list), 2))

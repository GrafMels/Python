# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

# *Примеры:*

# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

print('Введите дробное число через точку: ')
number = float(input())

number %= 1

print(int(number * 10))

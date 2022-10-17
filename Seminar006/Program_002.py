# 1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.

input_string = input('Введите выражение: ')


input_list = input_string.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ').split() 

dictionary = {
    '+': lambda x, y: str(float(x) + float(y)),
    '-': lambda x, y: str(float(x) - float(y)),
    '*': lambda x, y: str(float(x) * float(y)),
    '/': lambda x, y: str(float(x) / float(y)),
}

for i in range(len(input_list)):
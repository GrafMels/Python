# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.
first_string = input('Введите искомую строку: ')
second_string = input('Введите строку в которой будем искать: ')

count = 0

for i in range(len(second_string)+1):
    string_len = len(first_string)+i
    if first_string == second_string[i:string_len]:
        count += 1
print(count)
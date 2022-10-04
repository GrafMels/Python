# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.
first_string = input('Введите искомую строку: ')
second_string = input('Введите строку в которой будем искать: ')
string_len = 0
count = 0

for i in range(len(second_string)-1):
    if second_string[i] == first_string[0]:
        for j in range(len(first_string)-1):
            if second_string[i+j] == first_string[j]:
                string_len += 1
                if string_len == len(first_string)-1:
                    string_len = 0
                    count += 1

print(count)


        

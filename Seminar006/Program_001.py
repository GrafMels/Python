# Ввести с клавиатуры 2 числа (int) и вывести в консоль их НОК (наименьшее общее кратное)

var_1 = int(input('Введите первую переменную: '))
var_2 = int(input('Введите вторую переменную: '))

for i in range(min(var_1, var_2), var_1*var_2, min(var_1, var_2)):
    if i % var_1 == 0 and i % var_2 == 0:
        print(f'Наименьшее Общее Кратное: {i}')
        break
else:
    print(f'Наименьшее Общее Кратное: {var_1*var_2}')
        
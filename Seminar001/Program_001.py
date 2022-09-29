print('Введите два числа одно это квадрат другого: ')
num1 = int(input('Введите число 1: '))
num2 = int(input('Введите число 2: '))

if num1 ** 2 == num2 or num2 ** 2 == num1:
    print('Yes')
else:
    print('No')
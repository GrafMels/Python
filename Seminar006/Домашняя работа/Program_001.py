import math

d = float(input('Введите точность числа пи от 0.1 до 0.0000000001: '))

if d > 0.1 or d < 0.0000000001:
    print('Некорректное значение')
    
# count = 0

# for i in range(1, 11):
#     if d == (1/(10**i)): 
#         count = i

count = [i for i in range(1, 11) if d == (1/(10**i))]

print(round(math.radians(180), count[0]))



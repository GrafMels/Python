list = [None, None, None, None, None]

for i in range(0, 5):
    print(f'Введите число {i+1}: ')
    list[i] = int(input())

max = 0

for i in list:
    if max < i:
        max = i

print(f'Максимальное число: {max}')



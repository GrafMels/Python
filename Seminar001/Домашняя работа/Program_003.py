print('Введите кординаты точки на плоскости: ')
x = int(input('X: '))
y= int(input('Y: '))

if x > 0 and y > 0:
    print('Первая четверть')
elif x < 0 and y > 0:
    print('Вторая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
elif x > 0 and y < 0:
    print('Четвёртая четверть')
else:
    print('Точка лежит на оси')
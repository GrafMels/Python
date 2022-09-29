day_of_week = int(input('Введите день недели: '))

if day_of_week < 1 or day_of_week > 7:
    print(f'Дня недели с номером {day_of_week} не существует')
elif day_of_week > 5:
    print('Да. Это выходной')
else:
    print('Нет. К сожалению это не выходной')

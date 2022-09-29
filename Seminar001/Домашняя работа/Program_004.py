print('Введите нужный вам номер четверти')
num = int(input())

print('Координаты нужной вам четверти: 4')
if num == 1:
    print('X(1, ∞) Y(1, ∞)')
elif num == 2:
    print('X(-1, -∞) Y(1, ∞)')
elif num == 3:
    print('X(-1, -∞) Y(-1, -∞)')
elif num == 4:
    print('X(1, ∞) Y(-1, -∞)')
else:
    print('Такой четверти не существует')
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
print('Данная программа показывает правильно ли следующее утверждение: ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')

x = int(input('Введите x: '))
y = int(input('Введите y: '))
z = int(input('Введите z: '))

bool = not (x or y or z) == (not x and not y and not z)
print(bool)

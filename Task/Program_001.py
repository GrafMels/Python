print('Введите x: ')
x = int(input())
print('Введите y: ')
y = int(input())
print('Введите математический знак: ')
sign = input()

def mathematical_operation(x, y, sign):
    if sign == '+':
        return x+y
    if sign == '-':
        return x-y
    if sign == '/':
        return x/y
    if sign == '*':
        return x*y

print(f'{mathematical_operation(x,y,sign)}')





def View (data, operation_name, value_a, value_b):
    print(f'Результат: {value_a} {operation_name} {value_b} = {data}')

def getValue():
    return int(input('Введите значение аргумента: '))

def get_operation_name():
    return input('Введите знак операции: ')
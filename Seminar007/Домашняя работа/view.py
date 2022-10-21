import logger
import model


def error_value():
    logger.logger('Ошибка ввода данных')
    return print('Ошибка ввода данных')

def dev_by_zero():
    logger.logger('Деление на ноль')
    return print('Деление на ноль')


def print_total_str():
    return print(f'Результат: {model.full_string}')
import datetime


global path

path = 'log.txt'


def Log(result, oeration_name, value_a, value_b):
    string = f'{str(datetime.datetime.now())[:-7]}: {value_a} {oeration_name} {value_b} = {result}'
    with open(path, 'a', encoding='utf_8') as data:
        data.write(f'{string}\n')
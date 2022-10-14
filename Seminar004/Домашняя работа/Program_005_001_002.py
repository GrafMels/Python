import random

def polynomial(f, f_max):
    x = random.randint(-100, 100)
    x_max = random.randint(-100, 100)
    # Эта часть не получилась он не хочет сохранять юникод в файл, я не знаю почему¯\_(ツ)_/¯
    Unic = str(f-1) 
    # list_unicode = ['\u2070', '\u00B9', '\u00B2', '\u00B3', '\u2074', '\u2075', '\u2076', '\u2077', '\u2078', '\u2079']
    # Unic_list = []

    # for i in range(len(str(f-1))):
        
    #     for j in range(10): 
    #         if j == int(Unic[i]):
    #             Unic_list.append(list_unicode[j])
    # Unic = ''
    # for i in range(len(Unic_list)):
    #     Unic += str(Unic_list[i])
        
    
    if (f <= 1):# Последнее вхождение функции передаёт только рандом
        return ''
    else:
        if f == f_max: # Первое вхождение функции, в неё вносится два рандома
            if x_max < 0:
                return (f'{x}x^{Unic} {x_max}{polynomial(f-1, f_max)}')
            else:
                return (f'{x}x^{Unic} +{x_max}{polynomial(f-1, f_max)}')
        elif f == 2: # Пред последнее вхождение функции, икс в ней без степени
            if x < 0:
                return (f'x {x}{polynomial(f-1, f_max)}')
            else:
                return (f'x +{x}{polynomial(f-1, f_max)}')            
        else:
            if x < 0: # Все остальные вхождения
                return (f'x^{Unic} {x}{polynomial(f-1, f_max)}')
            else:
                return (f'x^{Unic} +{x}{polynomial(f-1, f_max)}')

f = int(input('Введите натуральную степень k для первого файла: '))
# f = 13

polynomial_string = ''
polynomial_string = str(polynomial(f+1, f+1))
print(polynomial_string)

my_file = open("File_005_1.txt", "w+")
my_file.write(polynomial_string)
my_file.close()

f = int(input('Введите натуральную степень k для второго файла: '))

polynomial_string = ''
polynomial_string = str(polynomial(f+1, f+1))
print(polynomial_string)

my_file = open("File_005_2.txt", "w+")
my_file.write(polynomial_string)
my_file.close()

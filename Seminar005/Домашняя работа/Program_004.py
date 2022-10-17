# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.

# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc
def Input_Output():
    with open('File_004_1.txt', 'r') as data_001:
        str_input = data_001.read()
    print(str_input)
    using_list = compression(str_input)
    print(using_list)
    str_output = expansion(using_list)
    with open('File_004_2.txt', 'w') as data_002:
        data_002.write(str_output)
    
def compression (string_in):
    list_in = []
    count = 0
    len_str = len(string_in)
    for i in range(len_str):
        if i == len_str-1:
            count += 2
            list_in.append(f'{count}{string_in[i]}')
            count = 0
        elif i == 0:
            count = 0        
        elif string_in[i] == string_in[i-1]:
            count += 1
        else:
            count += 1
            list_in.append(f'{count}{string_in[i-1]}')
            count = 0
    return list_in
        
def expansion (list_out):
    string_out = ''
    for i in range(len(list_out)):
        for j in range(int(list_out[i][:-1])):
            string_out += list_out[i][-1]
    return string_out
        
Input_Output()
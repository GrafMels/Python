num = str('qwe')

list = ['qwr', 'qwe', 'www', 'rrr', 'qwe', 'qwf', 'qqq']
my_list = []
my_bool = False
counter = 1
bool_ind = 0

for i in range(len(list)):
    bool_ind = list[i].find(num, bool_ind)
    if bool_ind == -1:
        my_bool = True
    if bool_ind != -1:
        bool_ind = list[i].find(num, bool_ind)
        counter += 1
        print(bool_ind)
        my_list.append(f'{list[i].find(num, bool_ind)}-й элмент {2}-e вхождение элемента')

    

if my_bool == False:
    print('Указаных символов не найдено')
else:
        print(f'{my_list}\n')
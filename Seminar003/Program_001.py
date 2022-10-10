num = str('he')

list = ['sg12432hewr', 'rerheqrh21124', 'qrhshehehehegjn4', 'rhshmdhedtu.,yryu.87', 'rhnaedherayeryh', 'aerhtjkhew45trh987', '45j54he6j3409u']
my_list = []
my_bool = False

for i in range(len(list)):
    counter = 0
    bool_ind = 0

    for j in range(len(list[i])):
        if list[i].find(num, bool_ind+j) != -1:
                bool_ind += list[i].find(num, bool_ind+j)
                counter += 1
    if counter > 0:
        my_bool = True
        my_list.append(f'{i+1}-й элемент списка: содержит {counter} указаных символов')
    else:
        my_list.append(f'{i+1}-й элемент списка: не содержит искомый символ')

if my_bool == False:
    print('Указаных символов не найдено')
else:
    for i in range(len(my_list)):
        print(my_list[i])
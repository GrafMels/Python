N = '0101010203030346034959595956989898987'

list_non_repeating = []

list_in_order = [i for i in range(10)]

list_in_order_num = []

for i in range(10):
    count = 0
    # for j in range(len(N)):
    #     if int(N[j]) == int(i):
    for j in enumerate(N):
        if int(j[1]) == int(i):
            count +=1
    list_in_order_num.append(count)
    if count == 1:
        list_non_repeating.append(i)

glued_list = list(zip(list_in_order, list_in_order_num))

for i in range(10):
    print(f'Частота попаданий в {glued_list[i][0]}: {glued_list[i][1]} раз')

print(f'Ответ: {list_non_repeating}')
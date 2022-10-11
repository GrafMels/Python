# Та же программа только для вещественных чисел. 
# Не работает
import random
import math
# колличество знаков после запятой, для того что бы выглядел красиво
number_of_characters = 6

number = 124.15161235

abs(number)
list_number_more = int(math.floor(number))
list_number_less = number % 1

list_number_less2 = math.modf(1.5)
round_for_simplification = len(str(list_number_less2[1]))

binary_list = []
binary_list_more = []

while list_number_more > 1:
    binary_list_more.append(int(list_number_more % 2))
    list_number_more = int(list_number_more / 2)
binary_list_more.append(list_number_more)

for i in range(len(binary_list_more)):
    binary_list.append(binary_list_more[-(i+1)])

binary_list.append('.')

counter = 0
list_number_less = round(list_number_less, round_for_simplification) * 2
while list_number_less != 1 and counter < 8:
    list_number_less = round(list_number_less, round_for_simplification) * 2
    if list_number_less > 1:
        binary_list.append(1)
        list_number_less -= 1
        
    else:
        binary_list.append(0)
    counter += 1
else: 
    binary_list.append(1)
    




for i in range(len(binary_list)):
    print(binary_list[i], end='')
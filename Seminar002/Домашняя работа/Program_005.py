from random import randint

N = int(input('Введите число: '))
X = 9
list = []

for i in range(N):
    list.append(randint(0, X))

print(list)

for i in range(N):
    rand_index = randint(0, N-1)
    switch_element = list[rand_index]
    list[rand_index] = list[i]
    list[i] = switch_element
    # print(list)
print(list)



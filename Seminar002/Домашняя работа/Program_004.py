from random import randint

N = int(input('Введите число: '))
list = []

for i in range(N):
    list.append(randint(-N, N))

print(list)

index_read_list = []
with open('file.txt', 'r') as data:
    index_read_list = data.read().split("\n")

multi = list[int(index_read_list[0])] * list[int(index_read_list[1])] * list[int(index_read_list[2])]

print(multi)
    



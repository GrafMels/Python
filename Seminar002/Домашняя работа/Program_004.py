from random import randint

N = int(input('Введите число: '))
list = []

for i in range(N):
    list.append(randint(-N, N))


with open('file.txt', 'w') as data:
    data.write(f"{str(list[i-1])}")
    for i in range(1,N):
        data.write(f"\n{str(list[i-1])}")
    data.close()

print(sum(list))


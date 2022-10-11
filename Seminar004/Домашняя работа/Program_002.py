# N = 444
N = int(input('Введите число: '))

list_prime_numbers = []
for i in range(2, N):
    count = True
    for j in range(2, i):
        if i % j == 0:
            count = False
    if count:
        list_prime_numbers.append(i)

list_prime_factor_numbers = []
coun = 0

for i in range(len(list_prime_numbers)):
    if N % list_prime_numbers[i] == 0:
        coun += 1
        list_prime_factor_numbers.append(list_prime_numbers[i])
        print(f'{coun}: {list_prime_numbers[i]} второй множитель {round(N / list_prime_numbers[i])}')

print(list_prime_factor_numbers)




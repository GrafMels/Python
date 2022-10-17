# N = 444
N = int(input('Введите число: '))

# list_range = []

# for i in range(2, N):
#     count = True
#     for j in range(2, i):
#         if i % j == 0:
#             count = False
#     if count:
#         list_prime_numbers.append(i)

list_range = [i for i in range(2,N)]

def filter_odd_num(in_num):
    count = True
    for i in range(2, in_num):
        if in_num % i == 0:
            count = False
    if count:
        return True
    else:
        return False

list_prime_numbers = list(filter(filter_odd_num, list_range))

# coun = 0

# for i in range(len(list_prime_numbers)):
#     if N % list_prime_numbers[i] == 0:
#         coun += 1
#         list_prime_factor_numbers.append(list_prime_numbers[i])
#         print(f'{coun}: {list_prime_numbers[i]} второй множитель {round(N / list_prime_numbers[i])}')

list_prime_factor_numbers = [list_prime_numbers[i] for i in range(len(list_prime_numbers)) if N % list_prime_numbers[i] == 0]

print(list_prime_factor_numbers)




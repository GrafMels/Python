def fibonacci(n):
    if (n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

n = int(input("Введите число членов последовательности:"))
print("Последовательность Фибоначчи:")

fibonachi_list = []
fibonachi_list_start = []

for i in range(n):
    fibonachi_list_start.append(fibonacci(i))

for i in range(1, n+1):
    if (n+i) % 2 == 0:
        fibonachi_list.append(-fibonachi_list_start[-i])
    else:
        fibonachi_list.append(fibonachi_list_start[-i])
    

for i in range(1, n):
    fibonachi_list.append(fibonachi_list_start[i])




print(fibonachi_list)
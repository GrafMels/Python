list = []

# for i in range(1,101,2):
#     list.append(i)


def f(x):
    return x**2

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ,12, 13, 14, 15, 16]

list1 = [(i, f(i)) for i in list if i % 2 == 0]
print(list1)

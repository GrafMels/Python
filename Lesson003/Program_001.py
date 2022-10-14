# def f(x):
#     return x**2

# print(type(f))

# g = f

# print(type(g))
# print(g(3))
# print(f(3))

# def calc1(x):
#     return x+10

# print(calc1(10))

# def calc2(x):
#     return x*10

# print(calc2(10))

# def math(op, x):
#     print(op(x))

# math(calc2, 10)
# math(calc1, 10)

# def sum(x, y):
#     return x+y

def mult(x, y):
    return x*y

def calc(op, a, b):
    print(op(a, b))
    return op(a, b)

calc(mult, 4, 5)
calc(lambda x, y: x+y, 4, 5)

print('Hello world')

aa = None
print(type(aa))
a = 123
b = 1.23
c = 'Fuuun \n yes'
aa = 1234

print(type(a))
print(type(b))
print(type(c))
print(type(aa))
print(c)

print(a, '-', b, '-', c)
print('{} - {} - {}'.format(a, b, c))
print(f'{a} - {b} - {c}')

d = True
print(d)

list = [1, 2, 3] #Массив короче
print(list)

print('Введите число х:')
x = input()

f = [1, 2, 3, 4]
print(2 in f)
print(5 in f)
print(not 2 in f)

is_odd = not f[0] % 2
print(is_odd)

q = int(input())
w = int(input())

if q > w:
    print(q)
elif q == w:
    print('q = w')
else:
    print(w)

original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Я забыл стоп слово')
print(inverted)

for i in 1,2,3,4,5:
    print(i**2)

listss = [1,2,3,4,5,6]

for i in listss:
    print(i**2)

r = range(4, 20, 2)#данная команда создаёт список(читать как массив) который выводит числа от 4 до 20 каждое второе

for i in r:
    print(i)

text = 'Заебался писать на питоне уйду в монастырь'

print(len(text))
print('писать' in text)
print(text.isdigit())
print(text.islower())
print(text.replace('писать', 'ебашить'))

for c in text:
    print(c)

print(text[:])


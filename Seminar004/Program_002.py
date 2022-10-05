# 2*x**2 + 4*x + 2 = 0
import math

with open("file_2.txt") as file:
    for line in file:
        data = str(line)
line = line.replace('- ','-')
string_split = line.split( )
print(string_split)

a_temp = str(string_split[0])
a1_temp = a_temp.split('*')
print(a1_temp)

b_temp = str(string_split[2])
b1_temp = b_temp.split('*')
print(b1_temp)

print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")


a = int(a1_temp[0])
b = int(b1_temp[0])
c = int(string_split[4])

 
discr = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discr)
 
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    result = "x1 = %.2f \nx2 = %.2f" % (x1, x2)
    print(result)
elif discr == 0:
    x = -b / (2 * a)
    result = "x = %.2f" % x
    print(result)
else:
    result = "No"
    print(result)


with open('MyFile_2.txt', 'w') as data:
    
    data.write(f'{result}')
    data.close()
with open("File_005_1.txt") as file:
    for line in file:
        data = str(line)

line = line.replace(' +',' ')
line = line.replace('x^',' ')
line = line.replace('x',' ')
string_split = line.split( )
list_term_1 = []

for i in range(int(string_split[1]) * 2):
    if i % 2 == 0:
        list_term_1.append(int(string_split[i]))
    elif i == (int(string_split[1]) * 2) - 1:
        list_term_1.append(int(string_split[i]))

print(list_term_1)
file.close()

with open("File_005_2.txt") as file:
    for line in file:
        data = str(line)

line = line.replace(' +',' ')
line = line.replace('x^',' ')
line = line.replace('x',' ')
string_split = line.split( )
list_term_2 = []

for i in range(int(string_split[1]) * 2):
    if i % 2 == 0:
        list_term_2.append(int(string_split[i]))
    elif i == (int(string_split[1]) * 2) - 1:
        list_term_2.append(int(string_split[i]))

print(list_term_2)
file.close()

list_term = []
difference = 0
max_len = 0

if len(list_term_1) > len(list_term_2):
    difference = len(list_term_1)-len(list_term_2)
    max_len = len(list_term_1)
    for i in range(difference):
        list_term.append(list_term_1[i])
    for i in range(len(list_term_2)):
        list_term.append(list_term_1[i+difference]+list_term_2[i])

elif len(list_term_2) > len(list_term_1):
    difference = len(list_term_2)-len(list_term_1)
    max_len = len(list_term_2)
    for i in range(difference):
        list_term.append(list_term_2[i])
    for i in range(len(list_term_1)):
        list_term.append(list_term_1[i]+list_term_2[i+difference])

else:
    max_len = len(list_term_1)
    for i in range(len(list_term_1)):
        list_term.append(list_term_1[i]+list_term_2[i])

polynomial = ''
for i in range(len(list_term)):
    if (max_len-1)-i == 1:
        polynomial += str(f' +{list_term[i]}x')
    elif (max_len-1)-i == 0:
        polynomial += str(f' +{list_term[i]}')
    elif list_term[i] > 0:
        polynomial += str(f' +{list_term[i]}x^{(max_len-1)-i}')
    else:
        polynomial += str(f' {list_term[i]}x^{(max_len-1)-i}')
    

print(polynomial)

with open("File_005.txt",'w') as file:
    file.write(polynomial)
file.close()



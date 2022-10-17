N = '0101010203030346034959595956989898987'

list_non_repeating = []
list_in_order = []

for i in range(10):
    count = 0
    # for j in range(len(N)):
    #     if int(N[j]) == int(i):
    for j in enumerate(N):
        if int(j[1]) == int(i):
            count +=1
    if count == 1:
        list_non_repeating.append(i)

print(list_non_repeating)
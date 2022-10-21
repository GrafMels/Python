import random
i = 0
for i in range(10):
    r=random.randint(0,10)
    if r % 2:
        i += 1
        print(r)

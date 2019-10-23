import random

minsoo = []
haram = []
yeram = []
for i in range(3):
    minsoo.append(random.randint(0,100))
    haram.append(random.randint(0,100))
    yeram.append(random.randint(0,100))
    
print(minsoo)
print(haram)
print(yeram)

sum = 0
for i in minsoo:
    sum += i
    minsoo.append(sum)
print(minsoo)

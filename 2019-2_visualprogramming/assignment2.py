import random


def lotto_generator(x):
    list = []
    number = random.randint(1,45)
    for i in range(6):
        while number in list:
            number = random.randint(1,45)
        list.append(number)
    return list


lottolist = []

for i in range(1000):
    lottolist.append(lotto_generator(i))
    print("%d회 : %s" % (i+1,lottolist[i]))

lottodict = {}
sum = 0

for i in range(1,46):
    for j in range(1000):
        count = lottolist[j].count(i)
        sum += count
    lottodict[i] = sum
    sum = 0

for i in list(lottodict.keys()):
    print("%d : %d회" % (i,lottodict[i]))

frequent = []
keylist = lottodict.keys()
for i in range(1000,0,-1):
    for j in keylist:
        if i == lottodict[j]:
            frequent.append(j)
        else:
            pass
print("이 주의 로또 번호 : %d,%d,%d,%d,%d,%d" % (frequent[0],frequent[1],frequent[2],frequent[3],frequent[4],frequent[5]))
            
        

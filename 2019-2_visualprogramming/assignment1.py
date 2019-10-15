import random
user1 = input('1. what is your name? ')
user2 = input('2. what is your name? ')
loca1 = 0
loca2 = 0
stage = 0


while True:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    stage += 1
    loca1 += dice1
    loca2 += dice2
    print(stage,'라운드: ',user1,'은', dice1,'가 나왔습니다.현재위치',loca1,'\n\t',user2,
          '는',dice2,'가 나왔습니다.현재위치',loca2)
    if loca1 > 30 or loca2 > 30:
        break

if loca1 > loca2:
    print(stage,'만에',user1,'가 이겼습니다.')
elif loca1 < loca2:
    print(stage,'만에',user2,'가 이겼습니다.')
else:
    print(user1,'와(과)',user2,'가 비겼습니다.')



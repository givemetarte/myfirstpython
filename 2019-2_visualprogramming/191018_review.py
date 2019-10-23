money = int(input('how much? '))

print('500원 %d개' % (money//500))
money = money % 500
print('100원 %d개' % (money//100))
money = money % 100
print('50원 %d개' % (money//50))
money = money % 50
print('10월 %d개' % (money//10))
money = money % 10
print('5원 %d개' % (money//5))
print('1원 %d개' % (money%5))





formula = input('수식을 입력하세요 : ')
number = ''
list = []
sum = 0

for i in formula:
    if i != '+' and i != '-':
        number += i
    else:
        if i == '+':
            list.append(number)
            number = '+'
        else:
            list.append(number)
            number = '-'
list.append(number)

for i in list:
    sum += int(i)
print('결과는 %d' % sum)


        

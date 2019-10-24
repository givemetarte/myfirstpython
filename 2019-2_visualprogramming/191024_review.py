data = input('수식을 입력하세요. 더하기만 가능. ')

numbers = data.split('+')
sum = 0

for i in numbers:
    sum += int(i)
print(sum)

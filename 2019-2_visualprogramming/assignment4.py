

import os
ufile = input('파일 이름을 입력하세요.: ')

scorelist = []

# 입력받은 파일이름이 없을 때 예외처리하고 다시 이름 받기
while True:
    try:
        f = open("%s.csv" % ufile, 'r', encoding='CP949')
    except FileNotFoundError:
        print('파일을 찾지 못했습니다!')
        ufile = input('파일 이름을 입력하세요.: ')
    else:
        print('파일을 찾았습니다!')
        lines = f.readlines()
        for line in lines[1:]:
            line = line[:-1]
            s = line.split(',')
            try:
                s.append(int(s[1])+int(s[2])+int(s[3]))
                s.append(int(s[1])+int(s[2])+int(s[3]))
                s.append(int(s[4])/3)
            except ValueError:
                print('데이터를 수정하세요.')
                s.append(0)
                s.append(0)
                s.append(0)
            scorelist.append(s)
        f.close()
        break


# 평균 리스트만 뽑기
averlist = []
for i in range(10):
    averlist.append(int(scorelist[i][-1]))
averlist.sort()
averlist.reverse()

# 평균을 가지고 같은 순서대로 집어넣으면 정렬이 됨.
ranklist = []
for i in averlist:
    for j in range(10):
        if i == scorelist[j][-1]:
            ranklist.append(scorelist[j])

# 파일 덮어씌울지 말지 정해서 파일 생성하기
if os.path.exists("/Users/harampark/Desktop/visualprogramming/_report.txt") == True:
    print('동일한 이름의 파일이 있습니다.\n 덮어씌우시겠습니까?')
    answer = input('예, 아니오로만 입력하세요.: ')
    if answer == '예':
        f = open("_report.txt", 'w', encoding='CP949')
    else:
        newName = input('새로운 이름을 입력하세요.: ')
        f = open("%s.txt" % newName, 'w', encoding='CP949')
else:
    f = open("_report.txt", 'w', encoding='CP949')
index = ['ranking', 'number', 'korean', 'English', 'Math', 'Sum', 'Average']
f.write("%7s %6s %6s %7s %4s %3s %7s\n" %
        (index[0], index[1], index[2], index[3], index[4], index[5], index[6]))
for i in range(7):
    f.write("%7d %6s %6s %7s %4s %3d %7.1f\n" % (
        (i+1), ranklist[i][0], ranklist[i][1], ranklist[i][2], ranklist[i][3], ranklist[i][4], ranklist[i][5]))
f.close()

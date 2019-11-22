# 1. 예외처리

scorelist = []

# 파일 열기
f = open("score.csv", 'r', encoding='CP949')
lines = f.readlines()
for line in lines[1:]:
    line = line[:-1]
    s = line.split(',')
    s.append(int(s[1])+int(s[2])+int(s[3]))
    s.append(int(s[4])/3)
    scorelist.append(s)
f.close()


# 평균 리스트만 뽑기
averlist = []
for i in range(10):
    averlist.append(scorelist[i][-1])
averlist.sort()
averlist.reverse()

# 평균을 가지고 같은 순서대로 집어넣으면 정렬이 됨.
ranklist = []
for i in averlist:
    for j in range(10):
        if i == scorelist[j][5]:
            ranklist.append(scorelist[j])

# report.csv 파일 만들기
f = open("report.csv", 'w', encoding='CP949')
index = ['ranking', 'number', 'korean', 'English', 'Math', 'Sum', 'Average']
f.write("%7s %6s %6s %7s %4s %3s %7s\n" %
        (index[0], index[1], index[2], index[3], index[4], index[5], index[6]))
for i in range(10):
    f.write("%7d %6s %6s %7s %4s %3d %7.1f\n" % (
        (i+1), ranklist[i][0], ranklist[i][1], ranklist[i][2], ranklist[i][3], ranklist[i][4], ranklist[i][5]))
f.close()

# 성적표 출력 함수
import os


def makereport(ranklist):
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
    index = ['ranking', 'number', 'korean',
             'English', 'Math', 'Sum', 'Average']
    f.write("%7s %6s %6s %7s %4s %3s %7s\n" %
            (index[0], index[1], index[2], index[3], index[4], index[5], index[6]))
    for i in range(7):
        f.write("%7d %6s %6s %7s %4s %3d %7.1f\n" % (
            (i+1), ranklist[i][0], ranklist[i][1], ranklist[i][2], ranklist[i][3], ranklist[i][4], ranklist[i][5]))
    f.close()

'''
f = open('score.csv', 'r')
while True:
    line = f.readline()
    if line == '':
        break
    for i in line:
        if i != '\n':
            pass
        else:
            line = line[:-1]
    score = line.split(',')
    score.append(int(score[1])+int(score[2])+int(score[3]))
    score.append(score[4]/3)
    print("%s의 점수는 국어: %s 수학: %s 영어: %s 총점: %d, 평균: %d입니다." %
          (score[0], score[1], score[2], score[3], score[4], score[5]))

f.close()
'''

try:
    f = open(filename, 'r')
except IOError:
    print('파일없음')
else:
    print('파일찾음')
    f.close()
finally:
    print('filename', '처리완료')

#1. 전자사전 만들기
dict = {}

f = open('dict_test_utf8.TXT','r')
lines = f.readlines()
for line in lines:
    if ' : ' not in line:
        pass
    else:
        line = line[:-1]
        wordlist = line.split(' : ')
        dict[wordlist[0]] = wordlist[1]
f.close()

uinput = input('단어를 입력하세요.: ')
while uinput != 'end': 
    if uinput in list(dict.keys()):
        print('%s의 뜻은 %s 입니다.' % (uinput,dict[uinput]))
    else:
        print('알 수 없습니다.')
    uinput = input('단어를 입력하세요.: ')


#2.끝말 잇기
list = []

# 파일 읽기 
f = open('dict_test_utf8.TXT','r')
lines = f.readlines()
for line in lines:
    if ' : ' not in line:
        pass
    else:
        line = line[:-1]
        wordlist = line.split(' : ')
        list.append(wordlist[0])
f.close()

usedlist = ['apple']

# 사전에 있는가? -> 단어가 5글자인가? -> 중복된 단어인가 -> 끝말잇기인가? 
uinput = input('%s의 끝말잇기는? ' % usedlist[-1])
while uinput != '끝':
    if uinput not in list:
        print('사전에 없는 단어입니다.')
    else:
        if len(uinput) != 5:
            if len(uinput) > 5:
                print('단어가 길어요.')
            else:
                print('단어가 짧아요.')
        else:
            if uinput in usedlist:
                print('중복된 단어입니다.')
            else:
                if usedlist[-1][-1] != uinput[0]:
                    print('끝말있기가 아닙니다.')
                else: 
                    usedlist.append(uinput)
    uinput = input('%s의 끝말잇기는? ' % usedlist[-1])



#3. 성적 처리하기 

scorelist = []

#파일 열기 
f = open("score.csv",'r', encoding='CP949')
lines = f.readlines()
for line in lines[1:]:
    line = line[:-1]
    s = line.split(',')
    s.append(int(s[1])+int(s[2])+int(s[3]))
    s.append(int(s[4])/3)
    scorelist.append(s) 
f.close()


#평균 리스트만 뽑기
averlist = []
for i in range(10):
    averlist.append(scorelist[i][-1])
averlist.sort()
averlist.reverse()

#평균을 가지고 같은 순서대로 집어넣으면 정렬이 됨. 
ranklist = []
for i in averlist:
    for j in range(10):
        if i == scorelist[j][5]:
            ranklist.append(scorelist[j])
            
#report.csv 파일 만들기 
f = open("report.csv",'w', encoding='CP949')
index = ['ranking','number','korean','English','Math','Sum','Average']
f.write("%7s %6s %6s %7s %4s %3s %7s\n" % (index[0],index[1],index[2],index[3],index[4],index[5],index[6]))
for i in range(10):
    f.write("%7d %6s %6s %7s %4s %3d %7.1f\n" % ((i+1),ranklist[i][0],ranklist[i][1],ranklist[i][2],ranklist[i][3],ranklist[i][4],ranklist[i][5]))
f.close()



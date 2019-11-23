# 파일이름 입력받고 데이터 읽는 부분

scorelist = []


def readdata():
    ufile = input('파일 이름을 입력하세요.: ')
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
    return scorelist

addDic = {'park':'ulsan','lee':'germany','choi':'seoul'}
telDic = {'park':'01033338888','lee':'01029873667','choi':'01029473826'}

uname = input('what\'s your name? ')
while uname != 'end':
    if uname in addDic:
        print('address:',addDic[uname],end=' ')
        print('tell:',telDic[uname],end=' ')
    else:
        print('that\'s new data.')
        add = input('address? ')
        telladd = input('tell? ')
        addDic[uname] = add
        telDic[uname] = telladd
        print(addDic,telDic)
    uname = input('what\'s your name? ')
        

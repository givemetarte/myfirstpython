str = "Not all that Mrs Bennet however with the assistance of her five daughters could ask on the subject was sufficient to draw from her husband any satisfactory description of Mr Bingley"


divstr = str.lower().split()
print(divstr)
strdic = {}

for i in divstr:
    strdic[i] = divstr.count(i)

keylist = list(strdic.keys())
print(keylist)

keylist.sort()

for i in keylist:
    print(i, strdic[i])

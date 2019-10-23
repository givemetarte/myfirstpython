
sen = "Not all that Mrs Bennet however with the assistance of her five daughters could ask on the subject was sufficient to draw from her husband any satisfactory description of Mr Bingley"
sen = sen.lower().split()

worddic = {}
for i in sen:
    if i not in worddic:
        worddic[i] = 1
    else:
        worddic[i] += 1

keylist = list(worddic.keys())

keylist.sort()

for i in keylist:
    print(i,worddic[i])

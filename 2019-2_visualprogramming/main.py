import readmodule
import writemodule


def makerank(scorelist):
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
    return ranklist


scorelist = readmodule.readdata()
ranklist = makerank(scorelist)
writemodule.makereport(ranklist)

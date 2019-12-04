def celtofah(cel):
    fah = ((9/5) * cel) + 32
    return fah  # 화씨


def fahtocel(fah):
    cel = (9/5) * (fah + 32)
    return cel


num = float(input('온도는? '))
print('섭씨 %f도는 화씨 %f 도이다' % (num, celtofah(num)))
print('화씨 %f도는 섭씨 %f 도이다' % (num, fahtocel(num)))

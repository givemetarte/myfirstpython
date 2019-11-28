from urllib.request import urlopen


def kakaoalarm(msg):
    # 카카오톡에서 허용을 받은 후에 사용하는 것.


while True:
    html = urlopen("http://google.co.kr")
    coinprice = int('0')
    if coinprice > 9000000:
        kakaoalarm('팔아라')
        # 카카오톡 메세지 보내기 api (사전에 등록한 사람들에 대해서 그 사람이 어떤 목적으로 카카오를 쓰겠다는 계획을 검토하고 문제가 없으면 허용)
        break
    time.sleep(60)
    # 그냥 두면 너무 빨리 돌아가서 이렇게 시간을 걸어줘야 함.

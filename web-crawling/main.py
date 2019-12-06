
from crapper import job_search
import pandas as pd


keyword = input('원하는 직무 분야를 입력하세요.: ')
new_keyword = ''
for word in keyword:
    if word == ' ':
        word = '+'
    new_keyword += word

HTML = f"https://kr.indeed.com/취업?q={new_keyword}&l="

df = pd.DataFrame(job_search(HTML))
df.to_csv('joblist.csv')

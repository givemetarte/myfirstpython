import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'AppleGothic'

while True:
    excel_file = 'elec.xlsx'
    df = pd.read_excel(excel_file)

    names = df['이름']
    rate = df['득표율']
    colors = ['yellowgreen', 'lightskyblue', 'lightcoral', 'grey']
    explodes = (0.03, 0.03, 0.03, 0.03)

    plt.pie(rate,
            labels=names,
            colors=colors,
            autopct='%1.2f%%',
            explode=explodes
            )
    plt.title('20대 선거 득표율', fontsize=20)
    plt.draw()
    plt.pause(10)
    plt.clf()

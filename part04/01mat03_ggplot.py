# -*- coding: utf-8 -*-
#라이브러리 임포트
import pandas as pd
import matplotlib.pyplot as plt

#한글깨짐처리
from matplotlib import font_manager, rc
font_path = "./data/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

#데이터프레임 만들기
df = pd.read_excel('./data/시도별 전출입 인구수.xlsx', engine='openpyxl', header=0)
df = df.fillna(method='ffill')
print(df.head())

#서울에서 경기로 전출할 데이터만 추출
mask = (df['전출지별']=='서울특별시') & (df['전입지별']!='서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)
print(df_seoul)
sr_one = df_seoul.loc['경기도']
print(sr_one)

#그래프 설정 및 데이터입력
##그래프 스타일 지정
plt.style.use('ggplot')
plt.figure(figsize=(14, 5))  
plt.xticks(rotation='vertical')
##마커와 마커사이즈 지정
plt.plot(sr_one.index, sr_one.values, marker='o', markersize=10) 

#타이틀 및 라벨, 범례 설정
plt.title('서울 -> 경기 인구 이동')
plt.xlabel('기간')
plt.ylabel('이동 인구수')
plt.legend(labels=['서울->경기'], loc='best') 

#그래프 출력
plt.show()


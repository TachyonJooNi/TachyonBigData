# -*- coding: utf-8 -*-
#라이브러리 임포트
import pandas as pd
import matplotlib.pyplot as plt

##한글깨짐처리start
from matplotlib import font_manager, rc
font_path = "./data/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
##한글깨짐처리end

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

##그래프 설정 추가 start
plt.figure(figsize=(14, 5))  
plt.xticks(rotation='vertical')
##그래프 설정 추가 end

# x, y축 데이터를 plot 함수에 입력
plt.plot(sr_one.index, sr_one.values)

#타이틀 및 라벨설정
plt.title('서울 -> 경기 인구 이동')
plt.xlabel('기간')
plt.ylabel('이동 인구수')

##범례 추가
plt.legend(labels=['서울->경기'], loc='best') 

#그래프 출력
plt.show()


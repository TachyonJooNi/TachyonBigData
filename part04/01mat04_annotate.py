# -*- coding: utf-8 -*-

# 라이브러리 임포트
import pandas as pd
import matplotlib.pyplot as plt

# 한글깨짐처리
from matplotlib import font_manager, rc
font_path = "./data/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 데이터프레임 만들기
df = pd.read_excel('./data/시도별 전출입 인구수.xlsx', engine='openpyxl', header=0)
df = df.fillna(method='ffill')
print(df.head())

# 서울에서 경기로 전출할 데이터만 추출
mask = (df['전출지별']=='서울특별시') & (df['전입지별']!='서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)
print(df_seoul)
sr_one = df_seoul.loc['경기도']
print(sr_one)

# 타이틀 및 라벨, 범례 설정
plt.title('서울 -> 경기 인구 이동')
plt.xlabel('기간')
plt.ylabel('이동 인구수')
plt.legend(labels=['서울->경기'], loc='best')
### 여기까지 ex03과 동일

# y축 범위를 지정한다.(최소값, 최대값)
plt.ylim(50000, 800000)

# 그래프에 주석을 표시한다. - 화살표
plt.annotate('',
             xytext=(2, 290000), # 화살표의 꼬리부분(시작점)
             xy=(20, 620000),    # 화살표의 머리부분(끝점)
             xycoords='data',    # 좌표체계
             # 화살표의 속성(서식) : 모양, 색깔, 두께를 딕셔너리로 지정
             arrowprops=dict(arrowstyle='->', color='skyblue', lw=2),
             )

plt.annotate('',
             xytext=(30, 580000),
             xy=(47, 450000),
             xycoords='data',
             arrowprops=dict(arrowstyle='->', color='olive', lw=5),
             )
# 그래프에 텍스트 주석을 표시한다.
plt.annotate('인구이동 증가(1970-1995)', # 출력할 텍스트 입력
             xy=(10, 450000),           # 텍스트의 위치(기준점)
             rotation=25,               # 회전각도
             va='baseline',             # 텍스트의 상하정렬
             ha='center',               # 텍스트의 좌우졍렬
             fontsize=15,               # 텍스트 크기
             )

plt.annotate('인구이동 감소(1970-2017)',
             xy=(40, 560000),
             rotation=-10,
             va='baseline',
             ha='center',
             fontsize=15,
             )
# 앞의 모든 설정을 저장한 후 그래프 출력
plt.show()


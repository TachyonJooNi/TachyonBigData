# -*- coding: utf-8 -*-
#데이터프레임 사용을 위해 판다스를 임포트
import pandas as pd
#데이터 시각화를 위해 맷플롯립 라이브러리를 임포트
import matplotlib.pyplot as plt

#엑셀파일을 데이터프레임으로 변환한다. header=0이므로 첫번째 행은
#타이틀로 인식하여 제외한다. 
df = pd.read_excel('./data/시도별 전출입 인구수.xlsx', engine='openpyxl', header=0)
#제일 먼저 상위 5개의 행을 확인한다. 누락값(NaN)이 다수 발견된다. 
#엑셀 파일의 병합된 셀에서 적절한 값을 찾지 못해 발생된다. 
print(df.head())

#누락값(NaN)을 앞 부분의 데이터로 채워준다.
df = df.fillna(method='ffill')
#NaN이 '전국'으로 대체된다. 
print(df.head())

'''
'전출지별' 열에서 '서울특별시'라는 값을 갖는 데이터만 추출한다. 
'전입지별' 열에서는 '서울특별시'가 아닌것만 추출한다. 
즉 서울에서 다른지역으로 이동한 데이터만 남게된다. 
'''
mask = (df['전출지별']=='서울특별시') & (df['전입지별']!='서울특별시')
df_seoul = df[mask]
#print(df_seoul)
# 전출지별 열(Column)을 삭제한다. 이때 반드시 axis=1옵션이 있어야한다.
df_seoul = df_seoul.drop(['전출지별'], axis=1)
#print(df_seoul)
#컬럼명을 변경하고, inplace옵션을 통해 기존 데이터프레임을 변경한다. 
#만약 inplace옵션이 없다면 새로운 데이터프레임 객체를 반환한다. 
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
#print(df_seoul)
#'전입지'를 인덱스로 설정한다. 
df_seoul.set_index('전입지', inplace=True)
print(df_seoul)


#서울에서 경기도로 전입한 데이터만 뽑아온다. 
sr_one = df_seoul.loc['경기도']
print(sr_one)


#x, y축 데이터를 plot 함수에 입력한다. 
plt.plot(sr_one.index, sr_one.values)


# 그래프의 제목과 x, y축의 타이틀을 추가한다. 
plt.title('서울 -> 경기 인구 이동')
plt.xlabel('기간')
plt.ylabel('이동 인구수')


#모든 변경사항을 저장한 후 그래프를 표시한다. 
plt.show()
#한글은 깨지고, x축 타이틀은 겹쳐져서 제대로 보이지 않는 문제가있다.
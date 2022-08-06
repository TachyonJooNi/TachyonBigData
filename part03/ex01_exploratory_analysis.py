# -*- coding: utf-8 -*-

import pandas as pd
'''
auto-mpg.csv
    : 자동차 연비를 데이터셋으로 구성한 파일이다.
    연비, 실린더수, 배기량 등의 데이터로 구성되어 있다.
'''
# CSV 파일을 데이터프레임으로 변환한다.
df = pd.read_csv('./data/auto-mpg.csv', header=None)
# 열 이름을 지정한다.
# [연비, 실린더, 배기량, 마력, 무게, 가속능력, 연식, 제조국 이름]
df.columns = ['mpg', 'cylinders', 'dixplacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

# 데이터프레임의 일부 데이터를 확인한다.
# 처음 5개의 행
print(df.head())
# 마지막 5개의 행
print(df.tail())

# df의 모양과 크기 확인 : 행의갯수, 열의갯수를 튜플로 반환한다.
print(df.shape)
# 내용 확인 : 클래스유형, 행인덱스, 열의이름과갯수, 자료형등이 출력됨
print(df.info())
# 자료형 확인
'''
int64 : 정수형
float64 : 실수형
object : 문자열
datetime64, timedelta64 : 날짜(및 시간)
'''
# 데이터프레임 전체의 자료형을 확인한다.
print(df.dtypes)
# 각 컬럼의 자료형을 확인한다.
print(df.mpg.dtypes)
print(df.cylinders.dtypes)

# 데이터 출력
print(df.describe())
print(df.describe(include='all'))

# 유효한 원소의 갯수
print(df.count())
print(type(df.count()))
# 특정 열의 고유값
unique_values = df['origin'].value_counts()
print(unique_values)

# 평균값
print(df.mean())
print(df['mpg'].mean())
print(df.mpg.mean())
print(df[['mpg', 'weight']].mean())

# 중간값
print(df.median())
print(df['mpg'].median())
print(df['origin'].median())

# 최대값
print(df.max())
print(df['mpg'].max())
print(df['horsepower'].max())

# 최소값
print(df.min())
print(df['mpg'].min())

# 표준편차
print(df.std())
print(df['mpg'].std())

# 상관계수
print(df.corr())
print(df[['mpg', 'weight']].corr())

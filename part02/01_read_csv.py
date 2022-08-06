# -*- coding: utf-8 -*-
import pandas as pd
'''
CSV(comma-separated values) 
    : 텍스트 파일의 일종으로 데이터를 쉼표(,)로 열을 구분하고, 
    엔터로 행을 구분한다. 엑셀을 통해 주로 생성한다. 
'''
file_path = './data/read_csv_sample.csv'

#read_csv() : CSV 파일을 데이터프레임으로 변환한다.
#옵션이 없으면 첫번째행은 제목으로 간주한다.  
df1 = pd.read_csv(file_path)
print(df1)

#제목이 없는것으로 간주하여 첫번째행부터 데이터를 가져온다. 
'''
header : 열의 이름으로 사용될 행의 번호를 기본값은 0이다. 
    만약 첫행부터 데이터가 있으면 None으로 지정하면된다. 
'''
df2 = pd.read_csv(file_path, header=None)
print(df2)

#index_col : 행의 인덱스로 사용할 열의 번호
df3 = pd.read_csv(file_path, index_col=None)
print(df3)

df4 = pd.read_csv(file_path, index_col='c0')
print(df4)

#names : 열의 이름으로 사용할 문자열 리스트
df5 = pd.read_csv(file_path, names=['손오공','저팔계','사오정'])
print(df5)

#skiprow : 처음 몇줄을 skip 할지를 설정한다. 
df6 = pd.read_csv(file_path, skiprows=2)
print(df6)


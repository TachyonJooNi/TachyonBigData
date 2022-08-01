# -*- coding: utf-8 -*-

import pandas as pd

# 딕셔너리를 데이터프레임으로 변환한다.
data = {'name' : ['Jerry', 'Rich', 'Paul'],
        'algol' : [ "A", "A+", "B"],
        'basic' : [ "C", "B", "B+"],
        'c++' : [ "B+", "C", "C+"],
        }

df = pd.DataFrame(data)
# 정수형 인덱스가 지정된 상태이다.
print(df)

# name열을 인덱스로 지정한다.
# 그러면 정수형 인덱스는 없어지고, name이 새로운 인덱스로 지정된다. 
# inplace=True 옵션으로 변경된 내용을 데이터프레임에 적용한다.
df.set_index('name', inplace=True) # --주석해제해가며 파일을 저장해보자.
print(df)

# 데이터프레임을 csv파일로 저장한다.
# set_index()를 통해 인덱스를 지정여부에 따라 CSV내용이 조금 달라진다.
df.to_csv("./save/df_sample.csv")
#df.to_csv("./save/df_sample2.csv")

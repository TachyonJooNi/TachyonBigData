# -*- coding: utf-8 -*-

import pandas as pd

exam_data = {'이름' : ['유비', '관우', '장비'],
             '국어' : [90, 80, 70 ],
             '영어' : [98, 89, 95],
             '수학' : [85, 95, 100],
             '체육' : [100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)

# 새로운 열(Column)을 추가한다. 행의 이름이 '역사', 모든 데이터는
# 80으로 초기화된다.
df['역사'] = 80
print(df)

# 새로운 행(Row)을 추가한다. 이때 이름과 데이터 모두 0으로 초기화된다.
df.loc[3] = 0
print(df)

# 새로운 행 추가.
df.loc[4] = ['제갈량', 90, 80, 70, 60, 50]
print(df)

# '장비' 행을 복사해서 마지막에 행을 추가한다.
df.loc['행5']= df.loc[2]
print(df)


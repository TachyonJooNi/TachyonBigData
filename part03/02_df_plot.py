# -*- coding: utf-8 -*-
'''
판다스는 Matplotlib 라이브러리의 일부를 내장하고 있어 별도의 임포트없이
그래프를 그릴 수 있다. 
'''
import pandas as pd

#엑셀파일을 데이터프레임으로 변환한다. 이때 첫행을 타이틀로 인식하여
#데이터에서는 제외된다. 즉 0행은 제외하고 1행부터 가져온다.
df = pd.read_excel('./data/남북한발전전력량.xlsx', engine='openpyxl')  

'''
첫번째행을 타이틀로 인식하여 (header=0 옵션) 제외된다. 
인덱스 0과 5는 각각 2행과 7열이므로 남한과 북한의 합계행을 선택한다. 
또한 A열이 인덱스0이므로 D행이 인덱스 3이된다. 
따라서 남한과 북한의 1991년부터 마지막년도인 2016년까지 전력량 합계 
데이터를 선택하여 변수에 저장한다. 
''' 
df_ns = df.iloc[[0, 5], 3:]            
# 행 인덱스를 변경한다. 
df_ns.index = ['South','North']        
# 열 이름의 자료형을 정수형으로 변경한다. 
df_ns.columns = df_ns.columns.map(int) 
print(df_ns.head())

#선 그래프1
df_ns.plot()

#선 그래프2
#클래스 속성인 T를 이용해서 데이터프레임을 전치한다. 
#즉 행과 열을 바꾸는것을 말한다. transpose()함수를 통해서도 전치할수있다. 
tdf_ns = df_ns.T 
print(tdf_ns.head())
tdf_ns.plot()

#막대 그래프
df_ns.plot(kind='bar')
tdf_ns.plot(kind='bar')

 




















# -*- coding: utf-8 -*-
"""
판다스는 Matplotlib 라이브러리의 일부를 내장하고 있어 별도의 임포트없이 그래프를 
그릴수 있다. 
"""
import pandas as pd

# 데이터프레임 변환 
df = pd.read_excel('./data/남북한발전전력량.xlsx', engine='openpyxl', thousands=',')  

'''
첫번째행을 타이틀로 인식(header=0 옵션임)하여 제외된다. 
인덱스 0과 5는 2행과 7열, 즉 남한과 북한의 합계 행이된다. 
또한 A열이 인덱스0 이므로 D행이 인덱스 3이 된다. 
따라서 남한과 북한의 1991년부터 마지막 년도인 2016년까지의 전력량합계를 선택한다. 
'''
df_ns = df.iloc[[0, 5], 3:]            
# 행 인덱스 변경
df_ns.index = ['South','North']        
# 열 이름의 자료형을 정수형으로 변경
df_ns.columns = df_ns.columns.map(int) 
print(df_ns.head())

#선 그래프
df_ns.plot()

# 클래스 속성을 통해 전치(행과 열을 바꿈)
tdf_ns = df_ns.T # df_ns.transpose() 와 동일함
print(tdf_ns.head())
tdf_ns.plot()

#막대 그래프
df_ns.plot(kind='bar')
tdf_ns.plot(kind='bar')

 






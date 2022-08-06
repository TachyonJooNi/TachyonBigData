# -*- coding: utf-8 -*-
import pandas as pd
import seaborn as sns
'''
데이터프레임 연산
    : 데이터프레임에 숫자를 사칙연산하면 모든 원소에 적용된다. 
    실행의 결과는 새로운 데이터프레임이 반환된다. 
'''

#seaborn에서 제공하는 타이타닉 탑승자 데이터셋을 로드한다. 
titanic = sns.load_dataset('titanic')

#타이타닉 데이터셋에서 age(나이), fare(운임) 2개열을 선택하여 데이터
#프레임을 만든다. 
df = titanic.loc[:, ['age','fare']]

#데이터프레임의 첫 5행을 출력
print(df.head())  
#마지막 5행을 출력
print(df.tail())  

#데이터프레임 전체에 10을 더한다. 
addition = df + 10
print(addition.head()) 

#데이터 프레임끼리 연산한다. 전체 데이터가 10이된다. 
subtraction = addition - df
print(subtraction.head())  



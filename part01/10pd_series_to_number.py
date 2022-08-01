# -*- coding: utf-8 -*-
'''
판다스의 산술연산
    단계1 : 행/열 인덱스를 기준으로 원소를 정렬한다.
    단계2 : 동일한 위치에 있는 원소끼리 일대일로 대응한다.
    단계3 : 일대일 대응이 되는 원소끼리 연산을 처리한다.
        그 이외에는 NaN 으로 처리한다.
        
시리즈 연산
    : 시리즈 객체에 숫자를 더하면 개별 원소에 각각 더해진 결과를
    반환한다.
'''
import pandas as pd
import numpy as np

# 딕셔너리로 시리즈 객체를 만든다.
student1 = pd.Series({'국어':100, '영어':80, '수학':90})
print(student1)

# 학생의 과목별 점수를 200으로 나눈다. 전체 데이터에 적용된다.
persentage = student1 / 200
print(persentage)

# 두번쨰 시리즈 생성. np.nan을 통해 NaN으로 초기화한다.
student2 = pd.Series({'수학':80, '국어':np.nan, '영어':80})
print(student2)

'''
사칙연산은 add(), sub(), mul(), div() 메서드를 사용할수있다.
공통 인덱스가 없거나 NaN이 포함되어 있으면 연산결과는 NaN이된다.
fill_value를 사용하면 NaN인 경우 지정한 값으로 대체할 수 있다.
'''
addition = student1 + student2
subtraction = student1 - student2
multiplication = student1.mul(student2, fill_value=0)
division = student1.div(student2, fill_value=0)

# 연산의 결과는 시리즈 객체이므로 이를 통해 데이터프레임을 생성한다.
# --이름이 있으면 똑같은 이름을 알아서 찾는다. (국어는 NaN이라 계산불가라 NaN)
# --나눗셈을 해서 나온 inf 는 무한대를 의미한다.
# --위에 판다스 산술연산의 단계에 나와있다.
result = pd.DataFrame([addition, subtraction, multiplication, division], 
                      index=['덧셈', '뺼셈', '곱셈', '나눗셈'])
print(result)
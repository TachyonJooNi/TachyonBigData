# -*- coding: utf-8 -*-


import pandas as pd

# 2개의 딕셔너리를 준비한다.
data1 = {'name' : ['Jerry', 'Rich', 'Paul'],
        'algol' : [ "A", "A+", "B"],
        'basic' : [ "C", "B", "B+"],
        'c++' : [ "B+", "C", "C+"]}
data2 = {'c0' : [1,2,3], 
         'c1' : [4,5,6],
         'c2' : [7,8,9], 
         'c3' : [10,11,12],
         'c4' : [13,14,15]}

# 데이터프레임으로 생성한 후 인덱스를 지정한다.
df1 = pd.DataFrame(data1)
df1.set_index('name', inplace=True)
print(df1)
print('\n')
      
df2 = pd.DataFrame(data2)
df2.set_index('c0', inplace=True)
print(df2)

# 각각의 데이터프레임을 지정한 sheet에 저장한다.
# --ExcelWriter()함수를 이용 엑셀파일을 만들어주고 sheet를 지정해 저장했다.
writer = pd.ExcelWriter("./save/df_excelwriter.xlsx")
df1.to_excel(writer, sheet_name="sheet1")
df2.to_excel(writer, sheet_name="sheet2")
writer.save()

# --JSP, Spring으로도 이런게 가능하지만 굉장히 복잡하다.

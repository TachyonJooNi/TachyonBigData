# -*- coding: utf-8 -*-
import pandas as pd

# HTML파일의 경로 혹은 웹URL을 통해 읽어온 웹페이지의 표(table)를
# 가져와서 데이터프레임으로 변환한다. 
url ='./data/sample.html'
tables = pd.read_html(url)

# 표의 갯수를 확인한다. 
print(len(tables))

# 표의 갯수만큼 반복하여 출력한다. 
for i in range(len(tables)):
    print("tables[%s]" % i)
    print(tables[i])
    print('\n')

#두번째 표를 변수에 저장한다. 
df = tables[1] 
#'name'열을 인덱스로 지정한다.     
df.set_index(['name'], inplace=True)
print(df)


 
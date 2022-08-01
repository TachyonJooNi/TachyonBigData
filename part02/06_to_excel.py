# -*- coding: utf-8 -*-

import pandas as pd

data = {'name' : ['Jerry', 'Rich', 'Paul'],
        'algol' : [ "A", "A+", "B"],
        'basic' : [ "C", "B", "B+"],
        'c++' : [ "B+", "C", "C+"],
        }

df = pd.DataFrame(data)
df.set_index('name', inplace=True)
print(df)

# to_excel()도 앞의 to_csv()와 사용법이 완전히 동일하다.
df.to_excel("./save/df_sample.xlsx")
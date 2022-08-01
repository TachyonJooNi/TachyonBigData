# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]

print(df.head())
print(df.tail())

addition = df + 10
print(addition.head())

subtraction = addition - df
print(subtraction.head())
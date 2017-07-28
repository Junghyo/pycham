'''
Created on 2017-07-28 12:50

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd

np.random.seed(0)
li = [x for x in np.random.randint(4000, 50000, 16)]
a = np.array(li).reshape(4, 4)
print(a)

df = pd.DataFrame(a, index = ["다음", "네이버", "넥슨", "NC"],
                  columns=[["7월", "7월", "8월", "8월"],["28일", "31일", "1일", "2일"]])
print(df)

# 컬럼명 변경.
df.columns.names = ["month", "day"]
print(df)

# 월별 합계
print(df.sum(level="month", axis=1))

# 일별 합계
print(df.sum(level="day", axis=1))

# 기업별 합계
print(df.sum(axis=1))
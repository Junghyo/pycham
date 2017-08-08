'''
Created on 2017-08-07 20:37

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as plt
import seaborn as sns
import scipy as sp
import scipy.stats as stats

# 5행 4열 데이터
np.random.seed(0)
df = pd.DataFrame(
    {
        "class": ["a", "a", "b", "b", "c"],
        "var1": np.arange(5),
        "var2": np.random.randn(5)
    },
    index=["r0", "r1", "r2", "r3", "r4"]
)

print(df)
#    class  var1      var2
# r0     a     0  1.764052
# r1     a     1  0.400157
# r2     b     2  0.978738
# r3     b     3  2.240893
# r4     c     4  1.867558

# 행 기준으로 선택해서 가져오기 (indexing and selection by row)
print(df.index)
# Index(['r0', 'r1', 'r2', 'r3', 'r4'], dtype='object')

# r0 행의 값들 가져오기
print(df.ix[0])
print(df.iloc[0])
print(df.ix["r0"])
print(df.loc["r0"])

# r2 행부터 데이터 가져오기
print(df.ix[2:])
print(df.iloc[2:])
print(df.ix["r2":])
print(df.loc["r2":])

# r1과 r4 데이터 가져오기
print(df.ix[[1, 4]])
print(df.iloc[[1, 4]])
print(df.ix[["r1", "r4"]])
print(df.loc[["r1", "r4"]])

# head : 행의 앞부분만 짤라서 보여줌
# 3행까지만 보고 싶다.
print(df.head(3))

# tail : 행의 뒤부분만 짤라서 보여줌
# 끝부분 2행만 보고 싶다.
print(df.tail(2))

# 열 기준으로 선택해서 가져오기 (indexing and selection by column)
div()
print(df.columns)
# Index(['class', 'var1', 'var2'], dtype='object')

# class열 데이터 가져오기
print(df["class"])
print(df.iloc[:, 0])
print(df.loc[:, "class"])

# var1 열부터 데이터 보기
print(df[["var1", "var2"]])
print(df.iloc[:, 1:])
print(df.loc[:, "var1":])

# class열과 var2열 데이터 보기
print(df[["class", "var2"]])
print(df.iloc[:, [0, 2]])
print(df.loc[:, ["class", "var2"]])

# r2행 var1열 데이터 확인
div()
print(df["var1"]["r2"])
print(df.iloc[2, 1])
print(df.loc["r2", "var1"])

# r2, r4행, class, var2열 데이터 확인
print(df.iloc[[2, 4], [0, 2]])
print(df[["class", "var2"]].iloc[[2, 4]])
print(df.loc[["r2", "r4"], ["class", "var2"]])
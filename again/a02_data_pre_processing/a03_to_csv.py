'''
Created on 2017-08-07 20:14

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

data = {
    "id": ["a1", "a2", "a3", "a4", "a5"],
    "x1": [1, 2, 3, 4, 5],
    "x2": [3, 4.5, 3.2, 4, 3.5]
}

df = pd.DataFrame(data, index=["r1", "r2", "r3", "r4", "r5"])
print(df)

# 결측값 추가
df2 = df.reindex(["r1", "r2", "r3", "r4", "r5", "r6"])
print(df2)

# 저장
# sep = "," 로 구분
# na_rep : 결측값 원하는 형태로 저장
df2.to_csv("z04_test.csv", sep=",", na_rep="-")

# na_values : 해당 값을 NaN으로 처리
df3 = pd.read_csv("z04_test.csv", index_col=0, na_values="-")
print(df3)
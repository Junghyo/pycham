'''
Created on 2017-08-07 20:28

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

"""
pd.DataFrame() 에서 사용하는 Paraeter 

(1) data, (2) index, (3) columns, (4) dtype, (5) copy 

(1-1) data : numpy ndarray, dict, DataFrame 등의 data source

(1-2) index : 행(row) 이름, 만약 명기하지 않으면 np.arange(n)이 자동으로 할당 됨

(1-3) column : 열(column) 이름, 만약 명기하지 않으면 역시 np.arnage(n)이 자동으로 할당 됨

(1-4) dtype : 데이터 형태(type), 만약 지정하지 않으면 Python이 자동으로 추정해서 넣어줌

(1-5) copy : 입력 데이터를 복사할지 지정. 디폴트는 False 임. 
(복사할 거 아니면 메모리 관리 차원에서 디폴트인 False 설정 사용하면 됨)

"""

df = pd.DataFrame(data=np.arange(12).reshape(3, 4),
                  index=["r0", "r1", "r2"],
                  columns=["c0", "c1", "c2", "c3"],
                  dtype="int",
                  copy=False)
print(df)

# 전치행렬 : T
print(df.T)

# axes : 행과 열 이름을 리스트로 반환
div()
print(df.axes)
# [Index(['r0', 'r1', 'r2'], dtype='object'), Index(['c0', 'c1', 'c2', 'c3'], dtype='object')]

# dtypes : 데이터 형태 반환
print(df.dtypes)
# c0    int32
# c1    int32
# c2    int32
# c3    int32
# dtype: object

# shape : 행과 열의 개수(차원)을 튜플로 반환
print(df.shape)
# (3, 4)

# size : df의 원소의 개수를 반환
print(df.size) # 12

# values : NDFrame의 원소를 numpy 형태로 반환
print(df.values)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# keys : 열의 이름 return
# columns
print(df.keys())
print(df.columns)
# Index(['c0', 'c1', 'c2', 'c3'], dtype='object')

# index : 행의 이름 return
print(df.index)
# Index(['r0', 'r1', 'r2'], dtype='object')


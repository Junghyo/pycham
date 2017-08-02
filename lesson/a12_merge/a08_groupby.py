'''
Created on 2017-08-02 18:32

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as plt

"""
Groupby

1. DataFrame이나 Series에서 데이터를 그룹
2. groupby(키) : 컬럼단위로 묶기
3. groupby : 메소드  ==> 새로운 인스턴스 생성..
4. DataFrameGroupBy 객체의 SeriesGroupBy 함수..
    1) count : NA제외 개수
    2) min, max : 최소값/최대값
    3) sum: 합계(NA제외)
    4) mean:평균(NA제외)
    5) median:중간값..
    6) var, std:분산과 표준편차
    7) prod : 누적곱셈(NA제외)
    8) first,last : 첫번째, 마지막값
    9) describe:요약
    
apply(함수명)
내부함수, 사용자정의 함수 모든 원소에 계산처..

"""
df = pd.DataFrame(
    {
        'key1':['a','a','b','b','a'],
        'key2':['one','two','one','two','one'],
        'data1':np.random.randn(5),
        'data2':np.random.randn(5)
    }
)
print(df)

# key1을 그룹화하여 데이터 나타내기
print(df.groupby(df["key1"]).mean())

# groupby : key1, data1만 보이기
print(df.groupby(df.key1).mean()["data1"])

# key1, key2를 그룹화
print(df.groupby([df.key1, df.key2]).mean())

# key1, key2 그룹화 data2만
print(df.groupby([df["key1"], df["key2"]])["data2"].mean())
print(df.pivot_table("data2", ["key1", "key2"]))

# 사전(dict)과 Series 묶기
div()
people = pd.DataFrame(np.random.randn(5,5), columns=['a','b','c','d','e'],
                   index =['joe','Steve','Wes','Jim','Travis'])
print(people)

# 2, 4행의 b, c열에 nan값
div()
people.ix[[2, 4],['b','c']] = np.nan
print("결측치 처리후 데이터\n",people)

## dict로 그룹을 설정.
div()
mapping ={'a':'black','b':'red','c':'blue','d':'blue','e':'red','f':'orange'}
print(people.groupby(mapping, axis=1).sum())
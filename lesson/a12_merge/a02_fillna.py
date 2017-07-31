'''
Created on 2017-07-31 15:42

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd

"""
 1. 초기에 data를 columns 매핑처리
    변수 01 = {key1 : [value1, ....]}
    
 2. 결측치(NaN)값에 대한 처리
    .fillna("결측치 NaN발생시, 대체할 문자열")
    
 3. DataFrame간 연결
    pd.concat([df1, df2], axis=1)
"""
stock1 = {
    "2017-07-28": [2000, 3000, 4000, 5000],
    "2017-07-31": [1111, 2222, 3333, 4444]
}

stock2 = {
    "2017-08-01": [9999, 8888, 7777],
    "2017-08-02": [1234, 5678, 4321]
}
index1 = ["daum", "naver", "nexen", "nc"]
index2 = ["daum", "naver", "nexen"]
# DataFrame
df1 = pd.DataFrame(stock1, columns=["2017-07-28", "2017-07-31"], index=index1)
df2 = pd.DataFrame(stock2, columns=["2017-08-01", "2017-08-02"], index=index2)
print(df1)
print(df2)

# concat() : axis=1
# fillna(값) : NaN를 원하는 값으로 변환
print(pd.concat([df1, df2], axis=1).fillna("-"))


"""
ex) 시청률 
닐슨, TNMS 합치기
"""
div()

data1 = {
    "2017-07-30": [31.0, 16.1, 15.2],
    "2017-07-29": [28.0, 15.8, 14.4]
}
data2 = {
    "2017-07-30": [32.4, 15.9, 14.7],
    "2017-07-29": [27.8, 16.8, 14.2]
}

df3 = pd.DataFrame(data1, columns=["2017-07-29", "2017-07-30"], index=["아버지", "언니", "당신"])

df4 = pd.DataFrame(data2, columns=["2017-07-29", "2017-07-30"], index=["아버지", "오리", "당신"])

print(pd.concat([df3, df4], axis=1).fillna("-"))

# join()
div()

print(pd.concat([df1, df2], axis=1, join="inner"))

# join_axes=["자정된 index"] 해당 index로 join 처리
div()
print(pd.concat([df1, df2], axis=1, join_axes=[df1.index]))
div()
print(pd.concat([df1, df2], axis=1, join_axes=[df2.index]))
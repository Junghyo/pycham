'''
Created on 2017-07-28 11:54

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd

"""
 계층적 index
 
 1. index나 컬럼이 2 level 이상으로 이루어진 경우(2차원 배열)
 2. 그룹화 연산에 유용
 3. 집계함수 level index나 컬럼 이름 대입, axis 축방향 댕비 설정.
"""

np.random.seed(0)
li = [x for x in np.random.randint(4000, 50000, 16)]
a = np.array(li).reshape(4, 4)
print(a)

df = pd.DataFrame(a, index = ["다음", "네이버", "넥슨", "NC"],
                  columns=[["7월", "7월", "8월", "8월"],["28일", "31일", "28일", "31일"]])
print(df)

# 7월의 데이터 가져오기
print(df["7월"])

# 7월 31일의 데이터 가져오기
print(df[("7월", "31일")])

# 7월 31일의 다음과 네이버 데이터 가져오기
div()
print(df["7월"]["31일"]["다음":"네이버"])
print(df[("7월", "31일")][0:2])

# 다음의 전체 데이터 가져오기
print(df[:1])

# 네이버 전체 데이터 가져오기
print(df[1:2])
print(df.ix[1])

"""
ex) 
이름, 투수, 방어율
이름, 타자, 타율

1. 기본 데이터 array
2. index 이름
colums = 방어율, 타율
"""

picther = {
    "avg": [0.385, 0.368, 0.362, 0.360, 0.343],
    "pos": ["타자", "타자", "타자", "타자", "타자"]
}
batter = {
    "avg": [2.84, 2.88, 2.93, 3.02, 3.19],
    "pos": ["투수", "투수", "투수", "투수", "투수"]
}




df1 = pd.DataFrame(picther, columns=["pos", "avg"], index=["김선빈", "최형우", "나성범", "김재환", "이명기"])
df2 = pd.DataFrame(batter, columns=["pos", "avg"], index=["차우찬", "박세웅", "피어밴드", "해커", "헥터"])
print(df1)
print(df2)
print(pd.merge(df1, df2, left_index=True, right_index=True, how="outer"))
'''
Created on 2017-08-01 09:58

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd

"""
 1. merge how()
    1) left : left join
    2) right
    3) outer
 
 2. suffixes
    tuple로 컬럼이름을 2개 대입하면 양쪽에 동일한 이름의 컬럼이 존재하는 경우
    컬럼 이름 뒤에 tuple의 값을 추가해 주는데 기본값 _x, _y
    
 3. index로 join
    left_index, right_index에 True로 설정
    
 4. sort
    key를 기준으로 정렬수행  
"""

stock1 ={'name':['다음','네이버','넥슨','NC'],
         '2017-07-28':[84900,818000,1756,292000],
         '2017-07-31':[86100,871000,1776,295000] }
stock2 ={'name':['다음','네이버','넥슨','KT'],
         '2017-08-01':[90800,766000,1695,300000],
         '2017-08-02':[90600,806000,1703,320000] }

# DataFrame
df1 = pd.DataFrame(stock1, columns=["name", "2017-07-28", "2017-07-31"])
df2 = pd.DataFrame(stock2, columns=["name", "2017-08-01", "2017-08-02"])
print(df1)
print(df2)


# inner
div()
print(pd.merge(df1, df2, how="inner"))

# outer
div()
print(pd.merge(df1, df2, how="outer"))

# left
div()
print(pd.merge(df1, df2, how="left"))

"right"
div()
print(pd.merge(df1, df2, how="right"))

## 데이터 한쪽에 없는 컬럼도 출력할려면 outer join(완전외부조인) 필요
## how = "outer" left/right
result = df1.merge(df2, on='name', how='outer')
print("="*20)
print(result)

## 특정한 컬럼을 index로 설정하는 경우..해당컬럼은 삭제..
print("="*20)
print(result['name'])

div()
result.index = result['name']
print(result)

## 컬럼의 삭제..
div()
result = result.drop('name', axis=1)
print(result)

## 행열 바꾸어 처리..
div()

result = result.T
print(result)
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

stock1 = {
    "name": ["daum", "naver", "nexen", "nc"],
    "2017-07-28": [2000, 3000, 4000, 5000],
    "2017-07-31": [1111, 2222, 3333, 4444]
}

stock2 = {
    "name": ["daum", "naver", "nexen"],
    "2017-08-01": [9999, 8888, 7777],
    "2017-08-02": [1234, 5678, 4321]
}

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


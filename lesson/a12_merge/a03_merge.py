'''
Created on 2017-08-01 09:42

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd

"""
 merge
 
 1. DataFrame이나 Series
    1) 첫번째, 두번쨰 데이터를 합침
        ex) pd.merge(df1, df2)

 2. 하나 이상의 key
    - 컬럼의 데이터가 동일한 key

 3. 데이터베이스 join연산 유사
    -key나 on에 명시된 컬럼 이름 기준으로 join
    
 4. on옵션에 컬럼 이름을 명시
    - join 기준 컬럼
      ex) on="name" : name컬럼 기준으로 조인
      
 5. 양쪽 데이터가 다른 경우 left_on/right_on 프레임의 컬럼이름 대입
    - 데이터베이스의 outer조인과 유사
    - 컬럼명이 다른 경우 alias이름 활용
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

div()

print(pd.merge(df1, df2))

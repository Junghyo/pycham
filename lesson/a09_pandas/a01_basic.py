'''
Created on 2017-07-27 12:11

@ product name : PyCharm Community Edition

@ author : yoda
'''
"""
 pandas
 
 효과적인 data 분석을 위한 고수준의 자료와 데이터 분석 도구 제공
 
 1차원 데이터 : Series를 통해 효과적으로 처리
 
 2차원 데이터 : DataFrame
 
 Series : 리스트 형태의 구조
 1) 정수 index + 값
 2) values : 데이터 값이 return
 3) index : 데이터 값에 매핑된 index
 4) 데이터 접근 : 변수명[index]
 
"""
import pandas as pd
import numpy as np
from mymod.print import *

price = pd.Series(np.arange(1000, 7000, 1000))
print(price)
print(price.index)
print(price.values)

for k, v in price.iteritems():
    print(k, ":", v)

div()

goods = pd.Series([1000, 5000, 4000, 3000], index=["apple", "orange", "grape", "strawberry"])
print(goods["apple"])
print(goods.values)
print(goods.index)

goods.name = "가격"
goods.index.name = "물건이름"
print(goods)

"""
ex)
전화번호 목록 작성
이름 전화번호
@@@ @@@@@
Series 이용 매핑 처리
"""

s1 = pd.Series(["123-1233", "222-1245", "344-7574"], index=["호날두", "메시", "루니"],
               name="전화번호부")
s1.index.name = "이름"
print(s1)
'''
Created on 2017-07-27 13:06

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd

"""
 pandas에서 지원하는 결측치(null) 관련 함수들
 
 1. isnull() : data가 없는 경우 true
 2. isnotnull() : data가 있는 경우 true
 
 pandas의 비교데이터 처리(결측치관련)
 1. None : 데이터 없음
 2. 결측치가 한쪽이라도 있으면 NaN으로 처리
"""

good1 = pd.Series([4000, 3000, 1000, 2000, None])
good1.index = ["orange", "apple", "grape", "melon", "kiwi"]
print(good1+2000)

good2 = pd.Series([700, 800, 200, None, 1000, 2000],
                  index=["grape", "apple", "melon", "strawberry", "kiwi", "grape"])

# 결측치 확인 : isnull()
print(good1.isnull())

# 연산처리
print(good1 + good2)

good3 = good1 + good2
print(good3[good3.notnull()])


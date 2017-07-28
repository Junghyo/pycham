'''
Created on 2017-07-28 11:19

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd

"""
 결측치 관련 처리
 
 1. isnull() : NaN 이나 False --> True ? False
 
 2. notnull() : isnull()의 반대
 
 3. dropna(how = , thresh = )
        how = all : 컬럼의 모든 값이 NaN인 경우만 제외
        thresh = 정수값5, 10 : 정수값 이상의 값을 소유한 컬럼 return
    
 4. fillna : NaN을 소유한 데이터 값을 특정한 값으로 변경
        method 매개변수로 이전/이후 값으로 채움
        lint 채울 개수 지정     
"""

stocks ={
        '2017-02-19':{'다음':50300,'네이버':51100, "넥슨":None, "NC":None},
        '2017-02-22':{'다음':50300,'네이버':50800, "넥슨":35000, "NC":None},
        '2017-02-23':{'다음':50800,'네이버':53000, "넥슨":37000, "NC":8000}
}

df = pd.DataFrame(stocks)
dft = df.T
print(dft)

# 결측치가 있는 행은 전부 제외
print(dft.dropna())

div()
print(dft.dropna(how="any"))
'''
Created on 2017-08-01 11:36

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd

"""
 replace(매개변수1, 매개변수2)
 1. 데이터 값 변경
 2. 매개변수1을 매개변수2로 대체
 3. list일 경우 치환처리
 4. dict(key, value) 치환가능

 rename()
 1. index, column 이름 변경
 
 2. index = 함수
    columns = 함수
    함수의 결과를 이용하여 변경
    
 3. dict(key, value) : key <---> value
 
 조건처리
 1. df[컬럼=데이터값] = 대입데이터
 2. Series의 데이터 순서 임의 변경
    numpy.random.permutation(갯수)
"""

stock = {
    "07-01": [2000, 3000, 4000],
    "07-02": [2700, np.nan, 2500]
}

df = pd.DataFrame(stock, index=["다음", "넥슨", "NC"])
print(df)

div()
df.reindex = ["daum", "nexen", "NC"]
print(df)
'''
Created on 2017-07-28 11:02

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd

"""
 statistics method
 
 1. axis : 계산방향. 0 - 행, 1 - 열.
 
 2. skipna : NaN값이 있는 경우 제외여부. T/F
 
 3. count, min, max, mean, var, std, quantile, argmin(최소값위치), argmax, idxmin(최소값색인)
 
 4. descirbe : 모든 통계치 요약
 
 5. 누적 통계량 : cumsum, cummin, cummax, cumprod
 
 6. diff : 산술차
 
 7. unique : 중복값은 배제하여 return - Series에서만 사용
 
 8. value_counts() : 빈도수 구하기. Series에서만 사용
"""

items = {
    "apple": {"count": 10, "price": 1500},
    "banana": {"count": 5, "price": 2000},
    "grape": {"count": 7, "price": 700},
    "orange": {"count": 8, "price": 500},
    "pineapple": {"count": 13, "price": 600},
    "kiwi": {"count": 3, "price": 2500},
    "mango": {"count": 17, "price": 3000},
    "lemon": {"count": 10, "price": 1200},
}

df = pd.DataFrame(items)
dft = df.T
print(dft)
print(dft.describe())

div()

apple = pd.read_csv("C:/pycharm/data/apple.csv")
print(apple)

samsung = pd.read_csv("C:/pycharm/data/samsung.csv")
print(samsung)

stocks ={
        '2017-02-19':{'다음':50300,'네이버':51100},
        '2017-02-22':{'다음':50300,'네이버':50800},
        '2017-02-23':{'다음':50800,'네이버':53000},
    }
data = pd.DataFrame(stocks)
data = data.T
print(data)
print("#"*15)
print(data.diff())

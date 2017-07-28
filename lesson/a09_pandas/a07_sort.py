'''
Created on 2017-07-28 10:46

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd

"""
 정렬(sort), 순위(rank)
 
 1. sort
 
    1) sort_index() : index로 정렬 처리. axis=1 대입시 열 단위
    
    2) 기본은 오름차순 정렬.
       내림차순 정렬시 ascending=False
    
    3) Series객체 : sort_values()
    
    4) 특정 컬럼 기준으로 정렬 : sort_values(by.컬럼이름, 컬럼리스트)
    

 2. rank
    
    1) rank() : 오름차순으로 순위를 설정
    2) ascending = False : 내림차순
    3) rank(axis=1) : 행 단위 
 
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

# by = 정렬 기준
print(dft.sort_values(by=["count", "price"]))

# count는 역순, price는 오름차순
print(dft.sort_values(ascending=[True, False], by=["count", "price"]))
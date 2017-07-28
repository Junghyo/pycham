'''
Created on 2017-07-28 09:43

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd

"""
 DataFrame 함수 적용
 1. apply(정의된 함수) 형식으로 행이나 열 단위로 적용
 
 2. apply(매개변수1, 매개변수2)
 매개변수1 : 함수선언
 매개변수2 : axis (defalut col단위  - 0)
 
 3. 데이터의 각각의 내용을 적용 - applymap 이용
 
 4. Series에 적용할 때, map 이용
        
"""

def func(x):
    return x.sum()

f = lambda x:x.sum()

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
print(df)
dft = df.T
print(dft)

# df.apply(함수명)
div()


print(dft.apply(func))
print(dft.apply(sum))

print(dft.apply(func, axis=1))
print(dft.apply(np.prod, axis=1))


# df.applymap(함수명) : 데이터 개별적으로 함수적용
def func2(x):
    return x + 10
print(dft.applymap(func2))

# count컬럼에만 10을 더하는 처리
# df["컬럼명"].map(함수명)
print(dft["count"].map(func2))

"""
 ex) 
 salesman의 실적
 이름 경비 수입
 
 함수: 수입 경비 합산액(수입-경비)
 1. 위 함수 적용
 2. 행단위로 나타내기
 3. 경비와 수입액에 환율이 적용되어 *10
 4. 수입액이 20% 상승 결과 출력
"""

df = pd.DataFrame(
    {
        "name": ["lee", "kim", "choi"],
        "sales": [3000, 2000, 2500],
        "cost": [1000, 1500, 1200]
    },
    columns=["name", "cost", "sales"]
)
print(df)

# 1. 수입 경비 합산액
print(df.apply(np.sum))
# 2. 행단위
df1 = df.set_index(["name"])
print(df1.apply(np.sum, axis=1))

# 3. 경비와 수입액에 환율 적용 * 10
def ex3(x):
    return x * 10
print(df1.applymap(ex3))

# 4. 수입액이 20% 상승
def ex3(x):
    return x + x * 0.2

print(df["sales"].map(ex3))

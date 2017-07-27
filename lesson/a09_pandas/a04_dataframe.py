'''
Created on 2017-07-27 14:41

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd

"""
 DataFrame : 여러개의 컬럼으로 구성된 2차원 형태의 자료구조
 
 1. dict 배열 유사
 
 2. dict를 이용해서 생성
    {key1: value1}
    {컬럼명1: [1,2,3,4,5}....}
 
 3. key는 정렬되어 배치
 
 4. 데이터 접근
    1) 프레임셋명["컬럼명"] col단위로 접근
    2) 프레임셋명[index번호] row단위로 접근

 5. 입력 가능 데이터
    1) 2차원 ndarry
    2) list, tuple, dict, Series
    3) dict, Series의 list
    4) list, tuple의 list
"""
items = {"code":[i for i in range(1, 7)],
         "name":["apple", "banana", "mango", "lemon", "grape", "orange"],
         "manufacture":["kor", "phil", "hawai", "kor", "chile", "kor"],
         "price":[1500, 2000, 3000, 2000, 5000, 3000]}

goods = pd.DataFrame(items)
print(goods)

# col단위로 데이터 가져오기
print(goods["name"])

# row단위로 데이터 가져오기(1 행)
print(goods[:1])
print(goods.ix[0])

# name컬럼의 1번째 데이터 가져오기
print(goods["name"][0])

"""
ex) 
프로야구 순위
순위  팀명  승   무   패   승률
"""
win = np.array([61, 54, 49, 49, 46, 49, 46, 38, 36, 29])
draw = np.array([0, 1, 1, 1, 1, 1, 2, 4, 1, 0])
lose = np.array([32, 37, 40, 44, 42, 46, 45, 53, 55, 63])
winrate = win/(win+draw+lose) * 100, 2
print(winrate)
data = {"team": ["kia", "nc", "doosan", "nexen", "lg", "sk", "lotte", "samsung", "hanhwa", "kt"],
        "win": [61, 54, 49, 49, 46, 49, 46, 38, 36, 29],
        "draw": [0, 1, 1, 1, 1, 1, 2, 4, 1, 0],
        "lose": [32, 37, 40, 44, 42, 46, 45, 53, 55, 63],
        "win rate": [ 65.59139785, 58.69565217, 54.44444444, 52.12765957, 51.68539326,
                      51.04166667,  49.46236559,  40.,  39.13043478,  31.52173913]
}
index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
baseball = pd.DataFrame(data, index=index, columns=["team", "win", "draw", "lose", "win rate"])
baseball.index.name = "rank"
print(baseball)

# 1. 두번쨰 팀 이름
print(baseball["team"][2])

# 2. 승률리스트
print(baseball["win rate"])

div()

goods1 = goods.T # 전치행렬
print(goods1)
# index를 다시 설정 : reindex()
goods2 = goods.reindex([1, 3, 4, 2, 5, 7])
print(goods)
print(goods2)

# 결측값은 0으로
goods3 = goods.reindex([1, 2, 3, 4, 5, 7], fill_value=0)
print(goods3)

# 결측값에 데이터 복사(마지막열)
goods4 = goods.reindex([1, 2, 3, 4, 5, 7], method="ffill", limit=2)
print(goods4)

div()
#데이터 삭제
goods5 = goods.T
print(goods5.index)
goods6 = goods5.drop("price")
print(goods6.T)
goods7 = goods.drop(goods[3], axis=1)
print(goods7)
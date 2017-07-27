'''
Created on 2017-07-27 15:50

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd

items = {
    "1": {"name": "apple", "manufacture":"kor", "price":1500},
    "2": {"name": "mango", "manufacture":"phil", "price":2000},
    "3": {"name": "melon", "manufacture":"jpn", "price":250},
    "4": {"name": "orange", "manufacture":"usa", "price":3000},
    "5": {"name": "grape", "manufacture":"chile", "price":1000},
    "6": {"name": "lemon", "manufacture":"kor", "price":500}
}

data = pd.DataFrame(items)
data01 = data.T
print(data)
print(data01)

# 데이터 추출

# 0~3행 ( 인덱스명으로 조회할 경우 끝자리까지 포함)
print(data01[0:3])

# price값이 1000이 넘는지 확인. boolean 값 return
print(data01["price"] > 1000)

# 1000원이 넘는 data들을 보고싶다면?
print(data01[data01["price"]>1000])

"""
 ex)
 1. index를 새로 처리해서 9위 구단을 삭제하고 모든 데이터 값을 0으로 처리
 2. 6위 행 삭제 처리
 3. 마지막 2개 데이터 drop으로 삭제 처리
 4. 1~4위까지 4개구단 정보만 데이터 할당 
 5. 승률이 50%이상인 구단 list 처리
"""
div()
win = np.array([61, 54, 49, 49, 46, 49, 46, 38, 36, 29])
draw = np.array([0, 1, 1, 1, 1, 1, 2, 4, 1, 0])
lose = np.array([32, 37, 40, 44, 42, 46, 45, 53, 55, 63])
winrate = win/(win+draw+lose) * 100, 2

data = {"team": ["kia", "nc", "doosan", "nexen", "lg", "sk", "lotte", "samsung", "hanhwa", "kt"],
        "win": [61, 54, 49, 49, 46, 49, 46, 38, 36, 29],
        "draw": [0, 1, 1, 1, 1, 1, 2, 4, 1, 0],
        "lose": [32, 37, 40, 44, 42, 46, 45, 53, 55, 63],
        "win rate": [ 65.59139785, 58.69565217, 54.44444444, 52.12765957, 51.68539326,
                      51.04166667,  49.46236559,  40.,  39.13043478,  31.52173913]
}
index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
baseball = pd.DataFrame(data, index=index, columns=["team", "win", "draw", "lose", "win rate"])
print(baseball)

# 1. 9위 구단 삭제(index 재배열) 및 모든 값 0
baseball1 = baseball.reindex([1, 2, 3, 4, 5, 6, 7, 8, 10])
baseball1[0:] = 0
print(baseball1)

# 2. 6위 행 삭제
print(baseball.drop(6))

# 3. 마지막 2개 데이터 drop으로 삭제 처리
print(baseball.drop([9, 10]))

# 4. 1~4위까지 4개구단 정보만 데이터 할당
print(baseball[:][0:4])

# 5. 승률이 50%이상인 구단
print(baseball[baseball["win rate"] >= 50])
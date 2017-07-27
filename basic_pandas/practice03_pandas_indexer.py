'''
Created on 2017-07-27 12:01

@ product name : PyCharm Community Edition

@ author : yoda
'''

"""
pandas indexer

pandas는 numpy 행렬과 같이 쉼표를 사용한 (행 인덱스, 열 인덱스) 형식의 인덱싱을
지원하기 위해 다음과 같은 특별한 indexer를 제공한다.

loc : 라벨 기반의 복수 인덱싱
iloc : 숫자 기반의 복수 인덱싱

"""

"""
 loc indexer
 
 loc 인덱서는 (행 인덱스, 열 인덱스) 형식의 인덱싱을 할 수 있지만 
 행/열 인덱서들이 모두 다음 중 하나이어야 한다.

정수 인덱스가 아닌 라벨 값(원래가 정수 인덱스인 경우는 예외)
라벨 값의 리스트
라벨 값의 슬라이싱
불리언 리스트, 1차원 배열, 시리즈 (데이터프레임은 안된다.)
또는 데이터프레임을 입력으로 받고 위의 값을 반환하는 함수
"""
import pandas as pd
import numpy as np
from mymod.print import *

df = pd.DataFrame(np.arange(10, 22).reshape(3, 4), index=["r1", "r2", "r3"],
                  columns=["c1", "c2", "c3", "c4"])

print(df)

# 1행 1열 data 확인
print(df.loc["r1", "c1"])

# 2~3행 1열 data 확인
print(df.loc["r2":, "c1"])

# 1행의 모든 열 data 확인
print(df.loc["r1", :])

# 1, 3행, 2, 4열 data 확인
print(df.loc[["r1", "r3"], ["c2", "c4"]])

# c1행의 값이 10이  넘는 row(행) 데이터들만 출력
print(df.loc[df.c1>10, :])
print(df.loc[df.c1>10])

"""
loc 인덱서를 사용하면 하나의 행을 시리즈 자료형으로 뽑아낼 수 있다.
만약 loc 인덱서를 사용하지 않으면 슬라이싱을 해야 하는데 
이 경우에는 데이터프레임 자료형을 반환한다.
"""
div()

print(df.loc["r1",:])
# <class 'pandas.core.series.Series'>

print(df[:1])
# <class 'pandas.core.frame.DataFrame'>


# df.loc[:, df[:1] <= 11]  # 데이터프레임은 loc 인덱서에 넣을 수 없으므로 에러!

# 행 전체에 r1의 열값 중 11 이하인 열만 출력
print(df.loc[:, df.loc["r1", :] <= 11]) # 이렇게 해야 한다.

div()
print(df)
# 컬럼 c1에서 value > 12 여부를 boolean값 처리
def find_rows(x):
    return x.c1 >12

print(find_rows(df))

# 컬럼 c1에 대한 데이터 값이 12보다 큰 행 중에서 c3 열의 값만 확인
print(df.loc[find_rows(df), ["c3"]])

# loc indexer 사용시 하나만 넣을 경우에는 row를 선택
print(df.loc["r1"])
# loc를 사용하지 않으면 col 선택
print(df["c1"])

# 새로운 행 추가
df.loc["r4"] = [90, 91, 92, 93]
print(df)

# 새로운 열 추가
df["c5"] = [10, 20, 30, 40]
print(df)

"""
iloc indexer

iloc 인덱서는 loc 인덱서와 반대로 라벨이 아닌 정수 인덱스만 받는다.
"""
div()
print(df)
# 1행 2열 data값

print(df.iloc[0, 1])

# 1~2행, 3열 data값
print(df.iloc[:2, 2])

# 1행, 4~5열
print(df.iloc[0, -2:])

# 1~2행, 2~3열
print(df.iloc[0:2, 1:3])

 # 2, 4행 3, 5열
print(df.iloc[[1, 3],[2, 4]])

# 4행(마지막행) 데이터
print(df.iloc[-1])

# data update

# 마지막행 데이터 변경
df.iloc[-1] = df.iloc[-1] * 2
print(df)
# 3행, 4열 데이터 변경
df.iloc[2, 3] = -345
print(df)
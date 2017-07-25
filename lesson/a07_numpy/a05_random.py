'''
Created on 2017-07-25 12:32

@ product name : PyCharm Community Edition

@ author : yoda
'''

import numpy as np

# np.random.normal() : 데이터 1개 랜덤으로 생성
print(np.random.normal())

# size 설정 : 데이터 건수
print(np.random.normal(size=5)) # 5개 생성

# tuple로 행렬단위 random 처리. 2행 3열 만들기
a = np.random.normal(size=6).reshape(2, 3)
print(a)

b = np.random.normal(size=(2, 3))
print(b)

# seed : random data가 동일한 내용을 한번 실행한 후, 계속 나타나야 할 필요성이 있을 경우
#        고유번호를 등록하고 실행마다 같은 내용을 처리한다.

# np.random.seed(seed=100)
print(np.random.normal(size=5))
print(np.random.normal(size=5))
print(np.random.normal(size=5))
# seed 설정 전에는 data가 계속 random하게 바뀌나 seed 설정 후에는 바뀌지 않음


"""
 ex)
 가위, 바위, 보 배열을 만들고 위의 데이터를 랜덤으로 하나만 나오게 처리하세요.
"""

game = np.array(["가위", "바위", "보"])
print(game)
# random_integers(start, end, 갯수) 정수범위
idx = np.random.random_integers(0, 2, 1)
print(game[idx])

# 2개
idx = np.random.random_integers(0, 2, 2)
print(game[idx[0]], game[idx[1]])
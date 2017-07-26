'''
Created on 2017-07-26 11:44

@ product name : PyCharm Community Edition

@ author : yoda
'''

"""
 prod() : 각 element를 곱셈(*) 처리
 
 sum() : 덧셈 처리
"""

import numpy as np

a = np.arange(1, 5)

print(a)

# prod() : *
print(a.prod())

# sum() : +
print(np.sum(a))

# 2차원 행렬 연산
c = np.arange(1, 5).reshape(2, 2)

print(c)

## axis=0 이면 열끼리 연산, axis=1 이면 행끼리 연산
print(c.prod(axis=0)) # 열 곱셈
print(c.prod(axis=1)) # 행 곱셈
print(np.sum(c, axis=0)) # 열 덧셈
print(np.sum(c, axis=1)) # 행 덧셈
print(c.prod()) # 전체 element 곱셈
print(np.sum(c)) # 전체 element 덧셈


"""
 ex)
 점심식사
 가격, 주문갯수
 총 비용을 처리(음식 종류 3개)   
"""
launch = np.array([[3000, 2], [4000, 3], [5000, 4]])
print(launch)
# 1. 각 음식별 총 금액
print(launch.prod(axis=1))
# 2. 총 합산 금액
print(sum(launch.prod(axis=1)))

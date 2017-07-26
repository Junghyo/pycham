'''
Created on 2017-07-26 12:45

@ product name : PyCharm Community Edition

@ author : yoda
'''


"""
 concatenate : 이항함수 - 배열 2개를 가지고 작업하는 함수
 
 여러개의 배열을 한개로 합치는 함수
 2차이상인 경우, x축과 y축 방향으로 합치는 2가지
 axis = 0 : y축(세로방향, 열)
 axis = 1 : x축(가로방향, 행)
 
 all the input arrays must have same number of dimensions
 all the input array dimensions except for the concatenation axis must match exactly
 axis = 0 일 경우에는 행의 수가 동일해야 하고
 axis = 1 일 경우에는 열의 수가 동일해야 함
"""

import numpy as np

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
print(np.concatenate((a, b)))    # [1 2 3 4 5 6 7 8]

print("=" * 50)
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print(a)
print(b)
# axis=0 : y축(세로)로 합침. a의 array의 기존 구조에 그대로 밑으로 b의 array를 붙임
print(np.concatenate((a, b), axis=0))
# axis=1 : x축(가로)로 합침. (a의 array의 기존 구조에 그대로 가로로 b의 array를 붙임)
print(np.concatenate((a, b), axis=1))


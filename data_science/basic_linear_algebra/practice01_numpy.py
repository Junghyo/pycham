'''
Created on 2017-08-01 15:33

@ product name : PyCharm Community Edition

@ author : yoda
'''

from mymod.print import *
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as plt

"""
데이터의 유형

선형대수에서 다루는 데이터는 개수나 형태에 따라 크게 
스칼라(scalar), 벡터(vector), 행렬(matrix)의 세 가지 유형으로 나누어진다.

간단하게 말하자면 
스칼라는 숫자 하나로 이루어진 데이터이고 
벡터는 여러 개의 숫자로 이루어진 데이터 레코드(data record)이며 
행렬은 이러한 벡터, 즉 데이터 레코드가 여러 개 있는 데이터 집합이라고 볼 수 있다.
"""

# scalar : 스칼라는 하나의 숫자만으로 이루어진 데이터를 말한다.
s1 = np.array(1)
# or
s2 = 1
print(s1)
print(s2)


# vector
div()
# numpy를 사용할 때는 벡터를 열의 개수가 하나인 2차원 배열 객체로 표현하는 것이 올바른 표현이다.
v1 = np.array([x for x in range(5)]).reshape(5, 1)
v2 = np.array([[5.1], [3.5], [1.4], [0.2]])
print(v1)
print(v2)
# 하지만 대부분의 경우에 NumPy는 1차원 배열 객체도 벡터로 인정한다.
# 이 경우에는 벡터가 마치 하나의 행처럼 표시되어도 실제로는 열의 의미를 가진다는 점에 주의한다.
v3 = np.array([x for x in range(5)])
print(v3)

# vector는 열의 수가 1인 행렬이라고 볼 수 있기 때문에
# 벡터를 다른 말로 열 벡터(column vector)라고도 한다.


# matrix
# numpy를 이용하여 행렬을 표기할 때는 2차원 ndarray 객체를 사용한다.
div()
m1 = np.array([[11, 12, 13], [21, 22, 23]])
print(m1)


"""
 전치 연산
 
 전치(transpose) 연산은 행렬에서 가장 기본이 되는 연산으로 행렬의 행과 열을 바꾸는 연산을 말한다.
 
 numpy에서는 ndarray 객체의 T라는 속성을 이용하여 전치 행렬을 구한다
"""
div()
print(m1.T)
print("shape before T :", m1.shape) # (2, 3)
print("shape after T :", m1.T.shape)# (3, 2)

# 다만 1차원 ndarray는 전치 연산이 정의되지 않는다.
v1 = np.array([1, 2, 3, 4])
print(v1)
print(v1.T)

"""
 special vector and matrix
"""
div()
# zero vector : 모든 원소가 0인  N 차원 벡터
z1 = np.zeros((3, 2))
print(z1)

# one vector : 모든 원소가 1인  NN 차원 벡터
o1 = np.ones((3, 2))
print(o1)

# square matrix : 행의 크기와 열의 크기가 같은 행렬. 정방 행렬
e1 = np.empty((3, 3))
print(e1)
# empty 껍데기 행렬. 각 element의 값은 의미가 없다.

"""
diagonal matrix

행렬에서 행의 숫자와 열의 숫자가 같은 위치를 대각(diagonal)이라고 하고 
대각 위치에 있지 않은 것들은 비대각(off-diagonal)이라고 한다. 
모든 비대각 요소가 0인 정방 행렬을 대각 행렬(diagonal matrix)이라고 한다.
"""
# 대각행렬의 값들이 1, 2, 3인 행렬
d1 = np.diag([1, 2, 3])
print(d1)

# 4x4 행렬에서 대각행렬 구하기
m1 = np.arange(1, 17).reshape(4, 4)
print(m1)
print(np.diag(m1))  # [ 1  6 11 16]
print(np.diag(m1, k=1)) # 오른쪽으로 1칸 밀린 대각행렬 [ 2  7 12]
print(np.diag(m1, k=-1))# 아래쪽으로 1칸 밀린 대각행렬 [ 5 10 15]

# identity matrix : 대각 행렬 중에서도 모든 대각 성분의 값이 1인 대각 행렬
# numpy로 단위행렬을 생성하려면 identity 혹은 eye 명령을 사용한다.
div()

i1 = np.identity(3) # 3x3 단위행렬 만들기
print(i1)
i2 = np.eye(4, 3, k=-1) # 4x3에 밑으로 한칸 밀린 단위행렬
print(i2)

# symmetric matrix : 전치 연산을 통해서 얻어진 전치 행렬과 원래의 행렬이 같으면
# 대칭 행렬(symmetric matrix)이라고 한다. 정방 행렬만 대칭 행렬이 될 수 있다.
div()

s1 = np.array([[1, 2, 3], [2, 3, 1], [3, 1, 2]])
print(s1)
print(s1.T)
# [[1 2 3]
#  [2 3 1]
#  [3 1 2]]